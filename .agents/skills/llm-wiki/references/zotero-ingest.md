# Zotero Ingest

Use this workflow whenever a source comes from Zotero or the user asks to repair Zotero metadata.

## Required order

1. Identify the bibliographic **parent item key** by exact title, DOI, citation key, or user-supplied
   key. Exclude `note` and `attachment` results.
2. Fetch metadata before full text:

   ```bash
   zotero-cli get metadata ITEM_KEY
   zotero-cli get bibtex ITEM_KEY
   zotero-cli get children ITEM_KEY
   zotero-cli get fulltext ITEM_KEY
   ```

3. Use the parent item's metadata as authoritative for Zotero identity. Use `children` only to
   capture attachment keys and filenames. Never substitute a PDF attachment key for the parent key.
4. Store a new raw record as `raw/papers/YYYY-MM-title-slug.md`, using the most precise publication
   year/month available and the wiki's lowercase kebab-case convention.
5. From `zotero-cli get fulltext`, keep only the text after its `## Full Text` transport heading;
   do not retain the CLI's duplicated title/metadata preamble. Preserve the extracted text bytes and
   normalize the assembled Markdown file to exactly one final newline.
6. Compute `sha256` over everything after the closing frontmatter delimiter, including the readable
   metadata block and extracted text after final-newline normalization.

If `zotero-cli` is unavailable, use an installed Zotero connector that returns the same fields. If
Zotero itself is unavailable, stop the Zotero ingest and report the blocker rather than silently
creating a metadata-free paper.

## Matching rules

Prefer identifiers in this order:

1. Exact Zotero parent item key
2. Exact DOI
3. Exact citation key
4. Exact normalized title plus publication year

When title search returns multiple candidates, compare DOI, year, and first author. Do not select a
candidate on title similarity alone. A `note` titled “Untitled” or a PDF `attachment` is never the
bibliographic parent.

## Raw frontmatter

Use YAML lists for authors, tags, collections, and attachment keys. Quote values containing YAML
punctuation. Keep unavailable optional fields absent rather than filling them with `unknown`.

```yaml
---
source_type: zotero
zotero_item_key: ZXT9CKFK
zotero_attachment_keys: [TRUJTFYP]
item_type: journalArticle
title: "CTI-Thinker: an LLM-driven system for CTI knowledge graph construction and attack reasoning"
authors:
  - Yang, Xiuzhang
  - Zhong, Ruijie
published: 2026-01-16
publication: Cybersecurity
volume: "9"
issue: "1"
pages: "106"
doi: 10.1186/s42400-025-00505-y
issn: 2523-3246
url: https://doi.org/10.1186/s42400-025-00505-y
language: en
citation_key: Yang2026_ZXT9CKFK
zotero_tags: [Attack reasoning, Cyber threat intelligence]
zotero_collections: [NK7LTLD6]
ingested: 2026-07-14
metadata_status: complete
sha256: <body-only-sha256>
---
```

Required for every Zotero paper:

- `source_type: zotero`
- `zotero_item_key`
- `item_type`
- `title`
- non-empty `authors`
- `published` (full Zotero date when available; otherwise the most precise supplied value)
- at least one stable locator: `doi`, `url`, or an arXiv identifier represented as a URL
- `ingested`, `metadata_status`, and `sha256`

Capture all available optional fields: publication/container title, publisher, volume, issue, pages,
DOI, ISBN/ISSN, URL, language, citation key, Zotero tags, collection keys, attachment keys, edition,
place, conference, and series. Preserve Zotero values; do not invent missing metadata from the PDF.

Set `metadata_status: incomplete` when a required field is missing, list the missing names in
`metadata_missing`, and tell the user. An incomplete record may be retained for repair but must not
be reported as a completed ingest.

## Readable metadata block

Place this immediately after frontmatter and before extracted text:

```markdown
# Paper Title

## Zotero Metadata

- Zotero Item Key: ZXT9CKFK
- Item Type: journalArticle
- Citation Key: Yang2026_ZXT9CKFK
- Authors: Yang, Xiuzhang; Zhong, Ruijie
- Published: 2026-01-16
- Publication: Cybersecurity 9(1):106
- DOI: 10.1186/s42400-025-00505-y
- URL: https://doi.org/10.1186/s42400-025-00505-y
- Attachment Keys: TRUJTFYP
- Tags: Attack reasoning; Cyber threat intelligence

## Abstract

<Zotero abstract, when present>

## Extracted Text

<Zotero full text>
```

Keep the abstract outside YAML to avoid large, fragile frontmatter. Repeat every available citation
field from frontmatter in the readable block, including ISSN/ISBN, collections, publisher, and
language when present, so humans can audit the record without parsing YAML. Do not include private
Zotero notes in the raw paper unless the user explicitly asks to ingest notes; notes are distinct
sources.

## Metadata completion and fallback

Zotero is authoritative for item identity and user curation. When an optional publication field is
missing, DOI, Crossref, publisher, or arXiv metadata may fill it only after matching a stable
identifier. Record the fallback source in `metadata_enriched_from`. Never overwrite a conflicting
Zotero value silently; retain both values or ask the user when the conflict changes citation identity.

## Backfill existing Zotero papers

When explicitly asked to repair old imports:

1. Inventory candidate files by existing Zotero key, DOI, URL, title, and year.
2. Resolve each file to exactly one parent item using the matching rules.
3. Save a copy of the original extracted-text portion in memory or a temporary comparison file.
4. Add or repair frontmatter and the `## Zotero Metadata` block only.
5. Verify that the extracted-text portion is byte-identical before and after the migration.
6. Recompute `sha256`, set `metadata_status`, and append one migration entry to `log.md` listing all
   updated files and unresolved items.

Keep an existing raw file at its current path during metadata backfill, even when it is under
`raw/articles/`; do not create a duplicate `raw/papers/` record or move immutable source content.
Only move it when the user explicitly requests a path migration, and update every `sources:` link in
the same operation.

Ask before a backfill that would modify 10 or more raw files. Do not create wiki concept pages as a
side effect of metadata-only repair.

## Lint checks

For every `source_type: zotero` record, report:

- missing required fields or an empty author list;
- `metadata_status: complete` despite missing requirements;
- duplicate `zotero_item_key` across raw files;
- attachment key used as `zotero_item_key`;
- frontmatter values that conflict with the readable metadata block;
- body hash mismatch;
- raw Zotero paper lacking `## Zotero Metadata` or `## Extracted Text`.
