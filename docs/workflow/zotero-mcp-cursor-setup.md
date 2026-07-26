# Zotero MCP ↔ Cursor 연결 가이드

> 문서 상태: 운영 치트시트  
> 작성일: 2026-07-24  
> 적용 대상: 이 저장소를 Cursor에서 열고 Zotero 라이브러리를 MCP로 조회할 때

이 문서는 **Cursor에 Zotero MCP를 다시 연결할 때** 보는 절차서다.  
canonical 지식이 아니라 `docs/` 산출물이며, API 키·userID 같은 비밀값은 넣지 않는다.

## 어떤 패키지를 쓰는지

이 템플릿 README가 가리키는 대상은 아래다.

- 권장: [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp) — CLI MCP 서버 (`zotero-mcp` / `zotero-cli`)
- 혼동 주의: [cookjohn/zotero-mcp](https://github.com/cookjohn/zotero-mcp) — Zotero **플러그인** 방식. Cursor `mcp.json`에 넣는 경로와 다름

논문 ingest 규칙은 `.agents/skills/llm-wiki/references/zotero-ingest.md`를 따른다.

## 사전 조건

- macOS에서 Zotero 데스크톱 **7+** (로컬 전문 접근 권장)
- Python **3.10+**
- Cursor (MCP 지원 클라이언트)
- (선택) [Better BibTeX](https://retorque.re/zotero-better-bibtex/installation/) — 인용키·주석 추출에 유리

## 1. Zotero Local API 켜기

1. Zotero를 실행한다.
2. **Settings → Advanced**로 이동한다.
3. **Allow other applications on this computer to communicate with Zotero**를 켠다.  
   (Zotero 9 기준 문구. 버전에 따라 메뉴 이름이 약간 다를 수 있다.)

Zotero는 MCP를 쓰는 동안 **켜 둔 상태**로 유지한다.

## 2. MCP 서버 설치

터미널에서 하나만 고른다. `uv` 권장.

```bash
uv tool install zotero-mcp-server
```

또는:

```bash
pip install zotero-mcp-server
# pipx install zotero-mcp-server
```

설치 확인:

```bash
which zotero-mcp
zotero-mcp setup-info
```

선택 extras (필요할 때만):

| Extra | 용도 |
| --- | --- |
| `[semantic]` | 의미 검색 |
| `[pdf]` | PDF outline 등 |
| `[all]` | 위 기능 일괄 |

```bash
uv tool install "zotero-mcp-server[all]"
```

## 3. Cursor에 등록

전역 설정 파일: `~/.cursor/mcp.json`

### 로컬 읽기 전용 (가장 단순)

API 키 없이 Local API만 사용한다.

```json
{
  "mcpServers": {
    "zotero": {
      "command": "zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

이미 다른 MCP가 있으면 `mcpServers` 객체 안에 `"zotero": { ... }`만 추가한다.

### GUI가 `zotero-mcp`를 못 찾을 때

Cursor는 shell `PATH`를 물려받지 않는 경우가 많다. `which zotero-mcp`로 나온 **절대 경로**를 `command`에 넣는다.

```json
"command": "/Users/YOUR_USER/.local/bin/zotero-mcp"
```

### 쓰기(하이브리드)까지 필요할 때

Local API는 읽기 위주이고, 라이브러리 쓰기(항목 추가·태그 등)는 Web API를 쓴다.

1. [Zotero Applications / API keys](https://www.zotero.org/settings/security#applications)에서 API key를 발급한다.
2. 같은 페이지의 **userID**(숫자)를 확인한다.
3. 아래 env를 채운다. **키와 ID는 이 문서·Git에 커밋하지 않는다.**

```json
{
  "mcpServers": {
    "zotero": {
      "command": "zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true",
        "ZOTERO_API_KEY": "YOUR_API_KEY",
        "ZOTERO_LIBRARY_ID": "YOUR_LIBRARY_ID"
      }
    }
  }
}
```

그룹 라이브러리면 `ZOTERO_LIBRARY_TYPE`을 `"group"`으로 두고, ID는 그룹 ID를 사용한다.

## 4. 연결 확인

1. Zotero 실행 + Local API ON
2. Cursor 재시작 또는 MCP 새로고침
3. Cursor **Settings → MCP**에서 `zotero`가 Connected인지 확인
4. 채팅 예시:
   - `Zotero 라이브러리에서 최근 논문 3개 검색해줘`
   - `제목에 transformer가 들어간 항목 찾아줘`

안 되면 공식 README 트러블슈팅을 본다: Local API 미활성, Zotero 미실행, `command` 경로 오류가 가장 흔하다.

## 5. 이 vault에서 쓰는 법

MCP 연결만으로 `raw/`에 자동 저장되지 않는다. Cursor 채팅에서 llm-wiki 스킬 흐름으로 지시한다.

```text
이 Zotero 논문 ingest 해줘: (제목 / DOI / item key)
```

ingest 시 에이전트는:

1. parent item 메타데이터 → children → fulltext 순으로 조회
2. `raw/papers/`에 출처 메타데이터와 본문을 보존
3. 필요하면 canonical 페이지·`index.md`·`log.md`를 갱신

상세 계약: `.agents/skills/llm-wiki/references/zotero-ingest.md`

## 관련 문서

- [README.ko.md](../../README.ko.md) — 도구 설치 표
- [SCHEMA.md](../../SCHEMA.md) — 위키 계약
- [knowledge-tool-roles](../../comparisons/knowledge-tool-roles.md) — Zotero vs 다른 도구 책임
- [llm-wiki](../../concepts/llm-wiki.md) — 원본·위키·스키마 계층
- 공식: https://github.com/54yyyu/zotero-mcp
- 문서 사이트: https://stevenyuyy.com/zotero-mcp/

## 보안

- `ZOTERO_API_KEY`를 저장소·스크린샷·채팅 로그에 남기지 않는다.
- `~/.cursor/mcp.json`은 개인 머신 설정이다. 이 vault에 복사해 커밋하지 않는다.
- 키를 유출했다면 Zotero에서 키를 폐기하고 재발급한다.
