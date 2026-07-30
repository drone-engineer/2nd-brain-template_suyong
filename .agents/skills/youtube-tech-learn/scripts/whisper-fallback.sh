#!/usr/bin/env bash
# [동작] 자막이 없거나 저품질일 때 yt-dlp + Whisper로 음성 전사
# [이유] 음악/OSD 자동자막만 있는 영상에서 실제 나레이션을 복구하기 위함
# Usage: bash whisper-fallback.sh VIDEO_ID
set -euo pipefail

VIDEO_ID="${1:-}"
if [[ -z "$VIDEO_ID" ]]; then
  echo '{"error":"VIDEO_ID required"}' >&2
  exit 1
fi

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CACHE="$SKILL_DIR/.cache/$VIDEO_ID"
mkdir -p "$CACHE"
OUT_TXT="$CACHE/whisper.txt"

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "{\"error\":\"$1 not found\",\"hint\":\"brew install $1 또는 pip install openai-whisper\"}" >&2
    exit 2
  }
}

need yt-dlp
need ffmpeg

URL="https://www.youtube.com/watch?v=${VIDEO_ID}"
AUDIO="$CACHE/audio.mp3"

echo "[whisper-fallback] downloading audio…" >&2
yt-dlp -x --audio-format mp3 -o "$CACHE/audio.%(ext)s" "$URL" >/dev/null

if command -v whisper >/dev/null 2>&1; then
  echo "[whisper-fallback] running openai-whisper…" >&2
  whisper "$AUDIO" --model small --language en --output_dir "$CACHE" --output_format txt >/dev/null
  # whisper writes audio.txt typically
  if [[ -f "$CACHE/audio.txt" ]]; then
    cp "$CACHE/audio.txt" "$OUT_TXT"
  else
    find "$CACHE" -name "*.txt" ! -name "whisper.txt" | head -1 | xargs -I{} cp {} "$OUT_TXT"
  fi
elif command -v whisper-cpp >/dev/null 2>&1 || command -v whisper-cli >/dev/null 2>&1; then
  echo "[whisper-fallback] whisper.cpp detected but model path not configured — install openai-whisper for default path" >&2
  exit 3
else
  echo '{"error":"whisper not found","hint":"pip install -U openai-whisper"}' >&2
  exit 2
fi

python3 - <<PY
import json, pathlib
p = pathlib.Path("$OUT_TXT")
text = p.read_text(encoding="utf-8").strip() if p.exists() else ""
print(json.dumps({
  "videoId": "$VIDEO_ID",
  "source": "whisper",
  "quality": "good" if len(text) > 80 else "poor",
  "text": text,
  "path": str(p),
}, ensure_ascii=False))
PY
