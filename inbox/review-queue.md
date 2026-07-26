# Review Queue (Human Gate)

> 파이프라인 `deliver-review` 결과. 사람이 Accepted / Contested / Deferred / Rejected를 적는다.  
> 이 파일은 `inbox/` — canonical 증거가 아니다.

## 사용법

1. 에이전트가 실행마다 아래에 블록을 **맨 위에** 추가한다.
2. 사람이 `판정:` 줄을 채운다.
3. Accepted만 장기 지식으로 유지. Rejected면 해당 canonical 변경을 되돌리거나 남기지 않는다.

---

## [2026-07-26] repair | raw 무결성 복구 + Gate B 확대

- **단계:** 감사 → repair → Gate B 확대 (canonical 내용 변경 없음)
- **발견:** raw 54건 중 해시 정상 17건뿐. Gate B가 `raw/papers/`만 봐서 가려져 있었음
  - 본문 오염 4건 (`notebooklm_source_id`가 frontmatter 밖에 삽입)
  - 닫는 `---` 누락 2건
  - 해시 계산 정의 불일치 26건
- **조치:** frontmatter만 수정하고 본문 바이트 보존 검증 → 49/54 해시 통과 (나머지 5건은 기존 legacy gap)
- **수집 스크립트:** 해시 계산·구분자 출력 버그 2건 수정 (재발 방지)
- **판정:**
  - 무결성 복구 + Gate B 확대 → **Accepted**
  - legacy web/youtube 5건 해시 소급 부여 → **Deferred** (원본 바이트 보존 우선)
- **사람 조치:**
  - [ ] 변경분 커밋 여부 결정 (fork `mine` 푸시)
  - [ ] Hermes Gateway 재가동 여부 결정 (현재 꺼져 있어 월요일 cron 미동작)

## [2026-07-26] collect | KCI 군집드론 운용 방안 (단일 수집)

- **단계:** collect-evidence (사용자 지시 URL 1건) → Gate A → review-queue prepend
- **수집 결과:** 신규 원본 1건
  - `raw/articles/2023-combat-swarm-drone-ai-operations-kci-ART003008075.md`
  - 출처: KCI `ART003008075` — 지능화 전장에서 인공지능 기반 공격용 군집드론 운용 방안 (2023)
  - KCI 피인용 1회 / FWCI 0.57 / 열람 3,492회
  - **누락:** 저자·학술지명·권호·발행년월은 KCI가 JS 변수로 렌더해 정적 추출 불가 → RIS/Citeasy 내보내기 또는 KCI API 권장
- **Gate A:** PASS (실재 URL, sha256 고정, 본문 불변)
- **canonical 변경:** 없음 (사용자 지시: 승인 없이 canonical 생성 금지)
- **사람 조치:**
  - [ ] 저자/저널 메타 보강 시 KCI RIS 내보내기로 `raw/articles/` 갱신 (Zotero 메타 repair 절차와 유사)
  - [ ] 이 원본을 canonical로 컴파일할지 결정 → 결정 시 `compile-wiki` 단계로 (UAV 군집 제어 주제이므로 기존 `concepts/uav-swarm-robotics.md` 등과 연결 가능)
- **판정:** Accepted (2026-07-26) — canonical `concepts/combat-swarm-drone-operations.md` 생성·연결 완료

## [2026-07-25] PDF meta repair + Alqudsi compile + KG refresh

- **단계:** PDF 재점검 → 메타 repair → canonical 보강 → understand-knowledge
- **PDF:** 여전히 2/9 (Alqudsi, AirSwarm). MDPI 자동 DL 403 재확인
- **repair:** `raw/papers/2025-01-…`, `2025-03-airswarm-…` attachment keys만 (Extracted Text 불변)
- **compile:** `concepts/uav-swarm-robotics.md` Alqudsi Table 6 요지; `entities/airswarm.md`; landscape 한계 문구
- **Gate B:** PASS · **`.ua/`:** 85 nodes / 77 edges (UAV 초점 analysis 1배치)
- **판정:**
  - Alqudsi PDF→canonical 과제표 → **Accepted** (이번 실행)
  - 나머지 7편 PDF → **Deferred** (사람 Find Full Text)
  - Tavily→Hermes 텔레그램 검색 배선 → **Deferred** (Cursor Tavily MCP는 동작 확인됨)
- **사람 조치:**
  - [ ] Zotero ❌ 7편 Find Full Text / 수동 첨부
  - [ ] (선택) Hermes에 Tavily 키 연결해 Telegram 웹검색

## [2026-07-25] PDF check + NotebookLM + Accepted compile

- **단계:** Zotero PDF 점검 → NotebookLM 질의 → review Accepted 반영
- **PDF:** 9편 중 2편만 로컬 첨부 (Alqudsi, AirSwarm). 상세 `docs/workflow/zotero-pdf-status.md`
- **NotebookLM:** 노트북 `UAV Swarm Survey Landscape` 생성, raw 9 + URL 4, 합성 질의 1회
- **compile:** `queries/uav-swarm-survey-landscape.md` 공백·읽기순서 증분 (Gate B PASS)
- **판정:**
  - UAV survey landscape 증분 → **Accepted**
  - ains-lab GitHub 테스트 클립 → **Deferred** (저가치, inbox 유지·raw 미승격)
  - 나머지 PDF 미확보 7편 재ingest → **Deferred** (사람 Find Available PDF 후)
- **사람 조치:**
  - [ ] Zotero에서 ❌ 7편 Find Available PDF
  - [ ] PDF 붙으면 Cursor에 재ingest 요청

## [2026-07-25] weekly collect+review (cron run 2)

- **단계:** collect(스캔) / review-queue prepend — canonical 자동 확정 없음
- **범위:** allowlist·사용자 요청 원본만 → `inbox/` 또는 등록된 `raw/` 경로
- **수집 결과:** 신규 수집 **없음**
  - allowlist/watch feed 미구성 — 수집은 사용자 "수집해줘: <URL/식별자>" 지시 또는 Zotero/Web Clipper 드롭으로만 구동
  - `inbox/` 미처리 신규 항목 없음 — 유일한 클립(ains-lab GitHub PNG 페이지 테스트 클립, 07-25)은 이전 블록에서 이미 확인됨. 저가치(캡처된 이미지 파일 페이지)로 raw 승격 보류
  - 대기 중인 사용자 수집 요청 없음
- **변경 요약:** raw/canonical 변경 없음. 이 review 블록만 prepend.
- **Gate 노트:**
  - Gate A(수집 무결성): 신규 원본 없음 → 검사 대상 없음
  - Gate B(canonical/index/log): 변경 없음, 기존 상태 유지 (index 14 pages, log tail 일관) — 이번 실행에서 재실행 안 함
  - raw 본문 불변 유지, Zotero 메타 복구 외 raw 편집 없음
- **사람 조치:**
  - [ ] 새 원본 수집: Telegram "수집해줘: <URL/식별자>" 또는 Zotero/Web Clipper 드롭
  - [ ] ains-lab 테스트 클립 유지/삭제 결정
- **판정:** _(미기재)_

## [2026-07-25] weekly collect+review (자동 실행)

- **단계:** collect(스캔) / review-queue prepend — canonical 자동 확정 없음
- **범위:** allowlist·사용자 요청 원본만 → `inbox/` 또는 등록된 `raw/` 경로
- **수집 결과:** 신규 수집 **없음**
  - allowlist/watch feed 미구성 (수집은 사용자 "수집해줘: …" 지시 또는 Zotero/Web Clipper 드롭으로 구동)
  - `inbox/` 미처리 항목 없음 — 유일한 클립(ains-lab 테스트 클립, 07-25)은 이미 캡처됨
  - 대기 중인 사용자 수집 요청 없음
- **변경 요약:** raw/canonical 변경 없음. 이 review 블록만 추가.
- **Gate 노트:**
  - Gate A(수집 무결성): 신규 원본 없음 → 검사 대상 없음
  - Gate B(canonical/index/log): 변경 없음, 기존 PASS 상태 유지 (14 pages) — 미재실행
  - raw 본문 불변 유지, Zotero 메타 복구 외 raw 편집 없음
- **사람 조치:**
  - [ ] 새 원본을 수집하려면 Telegram으로 "수집해줘: <URL/식별자>" 또는 Zotero/Web Clipper로 드롭
- **판정:** _(미기재)_

## [2026-07-25] Hermes Telegram + Cron online

- **단계:** gateway launchd + Telegram DM + cron `second-brain-collect-review`
- **스케줄:** 매주 월요일 09:00 KST → Telegram 전달
- **범위:** 수집·review-queue만 (canonical 자동 확정 금지)
- **사람 조치:**
  - [ ] 월요일 알림 오면 `inbox/review-queue.md` 판정
  - [ ] Accepted만 Cursor에서 canonical 반영
  - [ ] (선택) Telegram에서 수시 “수집해줘: …” 지시
- **판정:** _(미기재)_

## [2026-07-25] next-step: Clipper + Telegram prep

- **단계:** Telegram SDK 설치, 설정 가이드 작성, Clipper 재확인
- **완료:** `python-telegram-bot` 22.6, `docs/workflow/hermes/telegram-setup.md`, Zotero Connector 확인
- **Gate B:** 이전 PASS 유지 (그래프 `.ua/` 존재)
- **사람 조치 필요:**
  - [ ] Obsidian Web Clipper 설치 (Chrome)
  - [ ] BotFather로 봇 생성 → `hermes gateway setup`
  - [ ] `hermes gateway install` 후 Cron (telegram-setup.md C절)
- **판정:** _(미기재)_

## [2026-07-24] install-order tooling

- **단계:** Understand Anything 플러그인 + notebooklm-py + Hermes CLI 설치
- **Gate B:** PASS (재검증)
- **사람 조치 필요:**
  - [ ] Cursor 재시작 (UA 플러그인)
  - [ ] `notebooklm login`
  - [ ] `hermes model` 또는 `hermes setup`
  - [ ] (선택) `hermes gateway install` 후 Cron
- **판정:** _(미기재)_

## [2026-07-24] pipeline bootstrap

- **단계:** collect(기존 Zotero 9편 이미 ingest) / compile(UAV canonical 6) / graph=SKIP / review
- **Gate A:** 부분 통과 — 다수 항목 PDF 미첨부, abstract/메타 위주 (노트 명시됨)
- **Gate B:** 당시 수동 구성 (스크립트 도입 전). 이후 `python3 docs/workflow/check-gate-b.py`로 재검증 권장
- **Gate C:** SKIP — Understand Anything 미설치
- **변경 요약:** `raw/papers/` 9, UAV canonical 6, SCHEMA 태그/`raw/papers/` 등록, pipeline 문서
- **사람 조치 필요:**
  - [ ] Zotero에서 PDF `Find Full Text` / 첨부 후 본문 재ingest
  - [ ] UAV canonical 내용 검수 (Accepted 여부)
  - [ ] (선택) NotebookLM / UA / Hermes 도입 시기 결정
- **판정:** _(미기재)_
- **메모:**
