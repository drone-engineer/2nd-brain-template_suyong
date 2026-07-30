#!/usr/bin/env node
/**
 * [동작] YouTube URL → Google Data API 메타 + 자막 JSON
 * [이유] Skill / 웹앱이 같은 Evidence 파이프라인을 쓰도록 단일 스크립트로 고정
 * [근거] Data API = 공식 메타/설명, 자막 = TranscriptAPI 또는 youtube-transcript
 *
 * Usage: node fetch-evidence.mjs <youtube-url-or-id>
 * Env: YOUTUBE_API_KEY (권장), TRANSCRIPT_API_KEY (선택)
 */

import { writeFileSync, mkdirSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));

function extractVideoId(input) {
  const s = (input || "").trim();
  if (/^[\w-]{11}$/.test(s)) return s;
  const patterns = [
    /(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\s?#/]+)/,
    /youtube\.com\/embed\/([^&\s?#/]+)/,
    /youtube\.com\/shorts\/([^&\s?#/]+)/,
  ];
  for (const p of patterns) {
    const m = s.match(p);
    if (m?.[1]) return m[1];
  }
  return null;
}

function assessQuality(text, segmentCount) {
  const lower = text.toLowerCase();
  const musicHits = (lower.match(/\[music\]/g) ?? []).length;
  const words = text.replace(/\[[^\]]+\]/g, " ").split(/\s+/).filter(Boolean);
  const uniqueRatio =
    new Set(words.map((w) => w.toLowerCase())).size / Math.max(words.length, 1);
  if (segmentCount < 5 || words.length < 30) {
    return { quality: "poor", note: "자막이 너무 짧음" };
  }
  if (musicHits >= 3 || musicHits / Math.max(segmentCount, 1) > 0.3) {
    return { quality: "poor", note: "음악/[Music] 위주 자동자막" };
  }
  if (uniqueRatio < 0.25) {
    return { quality: "poor", note: "반복/OSD 위주 자막" };
  }
  return { quality: "good", note: "" };
}

function formatSegments(segments) {
  const cleaned = segments
    .map((s) => String(s.text || "").replace(/\s+/g, " ").trim())
    .filter(Boolean);
  const paragraphs = [];
  let buf = "";
  for (const line of cleaned) {
    buf = buf ? `${buf} ${line}` : line;
    if (buf.length >= 280 || /[.!?。]$/.test(line)) {
      paragraphs.push(buf.trim());
      buf = "";
    }
  }
  if (buf.trim()) paragraphs.push(buf.trim());
  return paragraphs.join("\n\n");
}

async function fetchGoogleMeta(videoId, apiKey) {
  if (!apiKey) return null;
  const url = new URL("https://www.googleapis.com/youtube/v3/videos");
  url.searchParams.set("part", "snippet,contentDetails,statistics");
  url.searchParams.set("id", videoId);
  url.searchParams.set("key", apiKey);
  const res = await fetch(url);
  if (!res.ok) {
    const t = await res.text();
    throw new Error(`YouTube Data API ${res.status}: ${t.slice(0, 200)}`);
  }
  const json = await res.json();
  const item = json.items?.[0];
  if (!item) return null;
  const sn = item.snippet || {};
  return {
    title: sn.title || "",
    channel: sn.channelTitle || "",
    description: sn.description || "",
    publishedAt: (sn.publishedAt || "").slice(0, 10),
    tags: sn.tags || [],
    thumbnailUrl:
      sn.thumbnails?.high?.url ||
      sn.thumbnails?.medium?.url ||
      `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`,
    duration: item.contentDetails?.duration || "",
    viewCount: item.statistics?.viewCount || "",
    source: "youtube-data-api",
  };
}

async function fetchOEmbed(videoId) {
  const canonical = `https://www.youtube.com/watch?v=${videoId}`;
  const res = await fetch(
    `https://www.youtube.com/oembed?url=${encodeURIComponent(canonical)}&format=json`,
  );
  if (!res.ok) return null;
  const o = await res.json();
  return {
    title: o.title || "",
    channel: o.author_name || "",
    description: "",
    publishedAt: new Date().toISOString().slice(0, 10),
    tags: [],
    thumbnailUrl:
      o.thumbnail_url || `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`,
    duration: "",
    viewCount: "",
    source: "oembed",
  };
}

async function fetchTranscriptAPI(videoId, apiKey) {
  if (!apiKey) return null;
  const res = await fetch(
    `https://transcriptapi.com/api/v2/youtube/transcript?video_url=${encodeURIComponent(`https://www.youtube.com/watch?v=${videoId}`)}&format=json`,
    { headers: { Authorization: `Bearer ${apiKey}`, Accept: "application/json" } },
  );
  if (!res.ok) return null;
  const json = await res.json();
  // API 스키마는 버전에 따라 다를 수 있어 방어적으로 파싱
  const segments =
    json.transcript ||
    json.segments ||
    json.data?.transcript ||
    json.data?.segments ||
    [];
  if (!Array.isArray(segments) || segments.length === 0) return null;
  const text = formatSegments(
    segments.map((s) => ({ text: s.text || s.content || "" })),
  );
  const { quality, note } = assessQuality(text, segments.length);
  return {
    text,
    lang: json.language || json.lang || "auto",
    segmentCount: segments.length,
    quality,
    qualityNote: note,
    source: "transcriptapi",
  };
}

async function fetchYoutubeTranscriptPkg(videoId) {
  const candidates = [
    join(__dirname, "../../../../cursor/Fulll-stack_B/2nd-brain-web/node_modules/youtube-transcript"),
    join(process.cwd(), "node_modules/youtube-transcript"),
    "youtube-transcript",
  ];
  let YoutubeTranscript;
  for (const c of candidates) {
    try {
      const mod = await import(c);
      YoutubeTranscript = mod.YoutubeTranscript;
      if (YoutubeTranscript) break;
    } catch {
      /* try next */
    }
  }
  if (!YoutubeTranscript) {
    return {
      text: "",
      lang: null,
      segmentCount: 0,
      quality: "none",
      qualityNote: "youtube-transcript 패키지 없음 — 2nd-brain-web에서 npm i youtube-transcript",
      source: "none",
    };
  }
  for (const lang of ["ko", "en", undefined]) {
    try {
      const segments = lang
        ? await YoutubeTranscript.fetchTranscript(videoId, { lang })
        : await YoutubeTranscript.fetchTranscript(videoId);
      const text = formatSegments(segments);
      if (!text) continue;
      const { quality, note } = assessQuality(text, segments.length);
      return {
        text,
        lang: lang || segments[0]?.lang || "auto",
        segmentCount: segments.length,
        quality,
        qualityNote: note,
        source: "youtube-transcript",
      };
    } catch {
      /* next lang */
    }
  }
  return {
    text: "",
    lang: null,
    segmentCount: 0,
    quality: "none",
    qualityNote: "자막을 가져오지 못함",
    source: "none",
  };
}

async function main() {
  const input = process.argv[2];
  if (!input) {
    console.error("Usage: node fetch-evidence.mjs <youtube-url-or-id>");
    process.exit(1);
  }
  const videoId = extractVideoId(input);
  if (!videoId) {
    console.error(JSON.stringify({ error: "invalid youtube url" }));
    process.exit(1);
  }

  const ytKey = process.env.YOUTUBE_API_KEY || "";
  const trKey = process.env.TRANSCRIPT_API_KEY || "";

  let meta = null;
  try {
    meta = await fetchGoogleMeta(videoId, ytKey);
  } catch (e) {
    meta = {
      error: e instanceof Error ? e.message : String(e),
    };
  }
  if (!meta || meta.error || !meta.title) {
    const oe = await fetchOEmbed(videoId);
    meta = oe
      ? { ...oe, googleError: meta?.error }
      : { title: `YouTube (${videoId})`, channel: "", description: "", thumbnailUrl: "", tags: [], source: "none", googleError: meta?.error };
  }

  let transcript = await fetchTranscriptAPI(videoId, trKey);
  if (!transcript) transcript = await fetchYoutubeTranscriptPkg(videoId);

  const result = {
    videoId,
    url: `https://www.youtube.com/watch?v=${videoId}`,
    meta,
    transcript,
    whisperRecommended:
      transcript.quality === "poor" || transcript.quality === "none",
    fetchedAt: new Date().toISOString(),
  };

  // 디버그용 캐시 (스킬 폴더)
  const outDir = join(__dirname, "..", ".cache");
  if (!existsSync(outDir)) mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, `${videoId}.json`), JSON.stringify(result, null, 2));

  process.stdout.write(JSON.stringify(result, null, 2));
}

main().catch((e) => {
  console.error(JSON.stringify({ error: e instanceof Error ? e.message : String(e) }));
  process.exit(1);
});
