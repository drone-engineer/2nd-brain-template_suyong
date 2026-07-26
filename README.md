# 2nd Brain Template

**English** | [한국어](README.ko.md)

> A Markdown-based knowledge management template for collecting scattered thoughts and information, connecting them, and turning them into action.

## Project Overview

This project goes beyond simply storing notes. It is designed around a continuous **capture → organize → connect → act → review** workflow. Every note is stored as a plain Markdown file, so the system is not tied to a particular application and can be used with Obsidian, VS Code, GitHub, or any other Markdown-compatible tool.

This fork is tuned for **UAV Swarm (군집드론) research** and is actively running: it ships a Hermes Agent cron, a NotebookLM increment workflow, and an automated free-OA paper collector (`docs/workflow/auto-collect-papers.py`).

### Architecture

The [complete architecture](docs/architecture/second-brain-pkm-architecture.md) consists of four layers: **Evidence → Canonical Memory → Discovery → Human Decision**. Original content and metadata are preserved as immutable evidence, while only reusable knowledge is compiled into canonical Markdown with traceable sources. Relationships discovered through NotebookLM and the knowledge graph remain hypotheses until human verification promotes them into durable memory.

![Evidence-based personal knowledge management architecture for the 2nd Brain](docs/architecture/second-brain-pkm-architecture.svg)

### Operating Workflow

The [operating workflow](docs/architecture/second-brain-pkm-architecture.md#6-핵심-워크플로우) follows **Capture → Compile → Discovery → Human Decision**. Each stage must pass integrity, frontmatter, and structural validation gates before moving forward. Approved changes update the canonical documents, index, and log together, then feed back into the knowledge graph and reusable outputs.

![2nd-Brain Evidence to Reusable Knowledge operating workflow](docs/workflow/second-brain-workflow.svg)

### Technology Stack

The core assets in the [technology stack](docs/architecture/second-brain-pkm-architecture.md#5-기술-스택) are not particular products, but **open-format source material, canonical Markdown, provenance metadata, and Git history**. Obsidian, Zotero, NotebookLM, and Understand Anything are replaceable tools for capture, editing, discovery, and analysis. Integrity checks and human approval gates connect the stack.

![2nd-Brain Durable Knowledge technology stack](docs/tech-stack/second-brain-technology-stack.svg)

## Key 2nd-Brain Features

The system connects safe source preservation and verified knowledge reuse in one continuous cycle.

| Feature | Description |
| --- | --- |
| **Source and provenance preservation** | Capture papers and web material with Zotero, arXiv/S2/OpenAlex APIs, then preserve the source, metadata, and SHA-256 digest under `raw/` so every claim can be traced back to evidence. |
| **Free OA auto-collection** | `docs/workflow/auto-collect-papers.py` pulls only open-access papers from arXiv, Semantic Scholar, and OpenAlex, de-duplicates, and downloads PDFs to `raw/papers/files/`. |
| **Verified knowledge compilation** | [LLM Wiki](concepts/llm-wiki.md) structures source material into concept, comparison, and query documents while accumulating provenance, confidence, contradictions, and relationships. |
| **Connected exploration and editing** | Follow the [second-brain research workflow](concepts/second-brain-research-workflow.md) to read and edit durable knowledge in Obsidian using Markdown, wikilinks, and backlinks. |
| **Source-grounded focused research** | Use the [NotebookLM query compounding workflow](queries/notebooklm-query-compounding.md) to question a constrained source set and file only results whose reuse value has been verified. |
| **Knowledge graph analysis** | Use the [UA knowledge graph workflow](queries/ua-knowledge-graph-workflow.md) to find clusters, bridges, isolated documents, and possible knowledge gaps, then verify graph results against the source material. |
| **Human verification and feedback** | The [research feedback loop](concepts/research-feedback-loop.md) classifies discoveries as accepted, contested, deferred, or rejected and feeds only approved knowledge back into the index and change history. |
| **Weekly automation** | Hermes Cron `second-brain-collect-review` (every Mon 09:00 KST) auto-collects new OA papers and refreshes `inbox/review-queue.md`, then reports to Telegram. |

## Prerequisites

If you only need a general Markdown editor, installing Obsidian is enough to get started. To use the full workflow—from web and paper capture to AI-assisted knowledge organization and graph exploration—prepare the tools below in order.

### Apps and Data Capture Tools

| Category | Tool | Purpose and installation |
| --- | --- | --- |
| Required | [Obsidian](https://obsidian.md/download) | Open this repository as a local vault to browse and edit Markdown notes. |
| Paper capture | [Zotero and Zotero Connector](https://www.zotero.org/download/) | Use the Zotero desktop application to manage papers, PDFs, and bibliographic data. Install the Chrome Connector from the same download page to save paper metadata from the web into Zotero. |
| Web capture | [Obsidian Web Clipper](https://obsidian.md/clipper) | Convert web pages and their metadata into Markdown from Chrome and save them to the Obsidian vault. |

### AI Automation Tools

The following tools allow an agent to retrieve captured material, organize it into knowledge notes, and visualize relationships. They are MCP servers, CLIs, or agent skills rather than Obsidian plugins.

> [!IMPORTANT] Install for your agent environment
> MCP configuration files, project and local skill paths, plugin support, and restart procedures differ between agents. Read the official installation documentation linked below and choose the method supported by your current agent or MCP client. Do not copy commands or configuration intended for a different agent without adapting them.

| Tool | Role | Installation guidance |
| --- | --- | --- |
| [Zotero MCP](https://github.com/54yyyu/zotero-mcp) | Gives an agent access to Zotero bibliographic metadata, attachments, notes, and full text. | Follow the official repository instructions to install and register the server with your MCP client. |
| [`llm-wiki`](https://github.com/ains-lab/harness/tree/main/skills/llm-wiki) | Compiles captured source material into an interlinked Markdown knowledge base with traceable provenance and validates the result. | Read the linked skill documentation together with your agent's skill installation guide, then install it in a supported local or project skill location. |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Manages NotebookLM notebooks and sources through a CLI and automates grounded questions and artifact generation. | Follow the official installation and authentication documentation for your Python and browser environment. |
| [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) | Analyzes relationships in code and knowledge bases and creates an interactive knowledge graph. | Select the installation and integration method for your agent or development environment from the official repository. |
| **Hermes Agent** (this fork) | Runs the weekly `second-brain-collect-review` cron and the `auto-collect-papers.py` collector. | Add `web` to `platform_toolsets.cli` in `~/.hermes/config.yaml`; link `llm-wiki` + `understand-knowledge` skills; register the cron with workdir set to this repo. |

> [!NOTE]
> `notebooklm-py` uses an unofficial Google API, so service changes may affect its behavior. Never commit authentication information such as Google login sessions or Zotero API keys to this repository.

### Recommended Installation Order

1. Install Obsidian and open this repository directory as a vault.
2. Install the Zotero desktop application, Zotero Connector, and Obsidian Web Clipper.
3. Review the supported environments and prerequisites at each official link above.
4. Follow the Zotero MCP documentation to connect Zotero to your current MCP client.
5. Install `llm-wiki` and Understand Anything according to both their official documentation and your agent's skill or plugin installation rules.
6. If needed, install `notebooklm-py` and complete authentication using its official documentation.
7. (This fork) Configure Hermes Agent `web` toolset and register the `second-brain-collect-review` cron.

After installation, use your environment's MCP server list, skill or plugin list, or CLI verification procedure to confirm that each tool is recognized. Follow the official documentation for exact verification commands and restart requirements.

## Recommended Directory Structure

The repository root is both the wiki root and the Obsidian vault. All paths are resolved relative to this root without a separate database, and [SCHEMA.md](SCHEMA.md) defines the validity contract for directories and data.

```text
.
├── inbox/                    # Temporary input awaiting classification and formal capture
├── raw/                      # Immutable source evidence
│   ├── articles/             # Article and web-clipping source text (arXiv/KCI records)
│   ├── notebooklm/           # Source records imported from NotebookLM
│   ├── papers/files/         # Paper attachments, created only when needed
│   ├── transcripts/          # Audio, video, and meeting transcripts
│   ├── web/                  # Web captures with importer-preserved paths
│   ├── youtube/              # YouTube metadata and transcripts
│   └── assets/               # Images and attachments referenced by source records
├── entities/                 # Canonical knowledge about people, organizations, and tools
├── concepts/                 # Canonical knowledge about concepts, principles, and methods
├── comparisons/              # Canonical side-by-side analysis of tools and methods
├── queries/                  # Source-grounded questions and synthesized answers
├── docs/                     # Architecture, workflow, and technology-stack artifacts
│   ├── architecture/
│   ├── tech-stack/
│   └── workflow/
├── templates/                # Validated note templates, created only when needed
├── _archive/                 # Fully superseded canonical knowledge, created only when needed
├── .obsidian/                # Shareable Obsidian configuration
├── SCHEMA.md                 # Authoritative directory, metadata, and integrity contract
├── index.md                  # Complete catalog of active canonical knowledge
└── log.md                    # Append-only wiki operation history
```

`raw/papers/files/`, `templates/`, and `_archive/` are created only when their workflows require them. Knowledge graph caches such as `.ua/` and other generated outputs are reproducible derived data, so they are not treated as canonical knowledge or source evidence.

### What the Structure Means

| Category | Location | Meaning and management |
| --- | --- | --- |
| Temporary intake | `inbox/` | Holds input whose source format and classification are not yet settled. These files are neither evidence nor canonical knowledge and should eventually be captured under `raw/` or removed. |
| Layer 1: source evidence | `raw/` | Preserves captured bodies and provenance metadata. After initial capture, the body is generally immutable; corrections and interpretation belong in canonical knowledge. |
| Canonical knowledge | `entities/ concepts/ comparisons/ queries/` | Durable, source-linked Markdown. Created only for a source's central subject or a subject repeated across at least two sources. |
| Deliverables | `docs/` | Architecture, workflow, and tech-stack diagrams. Not raw or canonical evidence. |
| Catalog and history | `index.md`, `log.md` | The index must equal the active canonical-file count; the log is append-only and never rewritten. |

## Current Status (this fork)

- **15 canonical pages** (concepts 5, queries 2, comparisons 1, entities 1, plus base pages)
- **30+ captured sources** — KCI 1 + arXiv 21 + Zotero 9
- **UAV swarm topics**: formation control, MARL, path planning, decentralized C2, swarm security, five autonomy pillars
- `concepts/combat-swarm-drone-operations.md` at `confidence: high`
- Automated collector wired to a weekly Hermes cron

---

Forked from [ains-lab/2nd-brain-template](https://github.com/ains-lab/2nd-brain-template). Extended as a UAV Swarm research example with live automation.
