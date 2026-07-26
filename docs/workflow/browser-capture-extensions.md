# 브라우저 캡처 확장 확인 가이드

Zotero Connector와 Obsidian Web Clipper가 설치·동작하는지 **브라우저에서** 확인한다.  
CLI로는 검증할 수 없다.

> 갱신: 2026-07-24  
> 대상: Chrome / Chromium / Arc / Brave (Chromium 계열). Safari·Firefox는 확장 스토어가 다름.

## 1. Zotero Connector

### 설치

1. [zotero.org/download](https://www.zotero.org/download/) 에서 **Zotero Connector** 링크를 연다.
2. Chrome 웹 스토어에서 **Add to Chrome** (또는 해당 브라우저 추가).
3. Zotero 데스크톱 앱이 실행 중이어야 저장이 된다.

### 확인

| 확인 | 기대 |
| --- | --- |
| 확장 아이콘 | 주소창 오른쪽 Zotero 아이콘(책/문서) |
| `chrome://extensions` | **Zotero Connector** 켜짐 |
| 논문 페이지(예: DOI, arXiv, IEEE) | 아이콘 클릭 → Zotero에 항목 추가 |
| Zotero 앱 | 새 항목이 My Library에 보임 |

실패 시:

- Zotero 앱이 꺼져 있으면 Connector가 저장하지 못한다 → 앱 실행 후 재시도.
- Local API / MCP와는 별개다. Connector는 **브라우저 → Zotero 앱** 경로다.

## 2. Obsidian Web Clipper

### 설치

1. [obsidian.md/clipper](https://obsidian.md/clipper) 에서 브라우저용 Clipper를 설치한다.
2. 확장 옵션에서 **Vault** = 이 저장소 폴더명(볼트로 연 이름)을 선택한다.
3. 기본 저장 위치를 `inbox/` 또는 `raw/web/` 로 맞춘다.  
   - 미분류면 `inbox/`  
   - 증거로 쓸 웹 캡처면 `raw/web/` (SCHEMA 등록 경로)

### 확인

| 확인 | 기대 |
| --- | --- |
| `chrome://extensions` | **Obsidian Web Clipper** 켜짐 |
| 아무 웹 페이지에서 Clipper 실행 | Markdown이 vault에 생성됨 |
| Obsidian / Finder | `inbox/` 또는 `raw/web/` 에 `.md` 파일 |

실패 시:

- Obsidian이 해당 폴더를 vault로 연 적이 없으면 Clipper가 vault 목록에 안 보일 수 있다 → Obsidian에서 **Open folder as vault** 후 Clipper 설정을 다시 연다.
- 생성된 파일은 곧바로 canonical이 아니다. `raw/` 형식·해시·ingest는 llm-wiki 흐름을 따른다.

## 3. 한 줄 체크리스트 (직접 표시)

브라우저에서 확인한 뒤 표시한다.

- [x] Zotero Connector 설치·활성 — Chrome Default에 확인됨 (2026-07-25)
- [ ] 논문 페이지 → Zotero에 저장 성공 (직접 한 번 테스트)
- [x] Obsidian Web Clipper 설치·활성 (2026-07-25)
- [x] Clipper vault = `2nd_Brain_Template`, 노트 경로 = `inbox`
- [x] 테스트 클립 → `inbox/` 에 파일 생성 확인 (2026-07-25)

## 4. 이 프로젝트에서의 위치

```text
브라우저 (Connector) → Zotero → (요청 시) Zotero MCP → raw/papers/
브라우저 (Web Clipper) → inbox/ 또는 raw/web/ → (요청 시) llm-wiki compile
```

확장만 설치해도 vault canonical은 자동으로 바뀌지 않는다. 수집과 위키 컴파일은 별 단계다.
