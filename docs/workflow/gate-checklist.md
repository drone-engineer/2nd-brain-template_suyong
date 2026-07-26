# Gate A / B / C 체크리스트

아키텍처 그림의 품질 관문. 하나라도 실패하면 다음 단계로 가지 않는다.

## Gate A — raw 무결성 (collect-evidence 후)

- [ ] 파일이 등록된 `raw/` 하위 경로에 있다 (`SCHEMA.md` Directory roles)
- [ ] frontmatter에 출처 식별자(URL/DOI/Zotero key 등)와 `ingested`가 있다
- [ ] Zotero면 `source_type: zotero`, parent `zotero_item_key`, authors, published, locator, `metadata_status`, `sha256`가 있다
- [ ] `sha256` = frontmatter 닫는 `---` 이후 body 바이트의 SHA-256
- [ ] 본문을 “고쳐서” 다시 쓰지 않았다 (해석은 canonical만)
- [ ] PDF/전문이 없으면 Extracted Text에 **명시적 note**가 있고, 완료로 과장하지 않았다
- [ ] `log.md`에 ingest 경로가 기록됐다
- [ ] 미분류 항목이 canonical `sources`에 올라가지 않았다

**통과 조건:** 위 항목 모두 예(또는 N/A가 정당한 경우).

## Gate B — wiki lint (compile-wiki 후)

빠른 검사:

```bash
python3 docs/workflow/check-gate-b.py
```

수동 확인:

- [ ] 모든 canonical 페이지: `title, created, updated, type, tags, sources, confidence, contested, contradictions`
- [ ] `type` ↔ 디렉터리 일치, 태그는 `SCHEMA.md` 등록분만
- [ ] `sources` 경로가 실제 raw 파일을 가리킨다
- [ ] 페이지당 서로 다른 활성 canonical `[[wikilink]]` ≥ 2
- [ ] `index.md` 항목 수 = 활성 canonical 파일 수, 알파벳·타입 섹션 정확
- [ ] `log.md`에 이번 변경이 append됨 (이전 항목 수정 없음)
- [ ] claim marker `^[raw/...]`는 해당 페이지 `sources`에 이미 있음

**통과 조건:** 스크립트 exit 0 + 위 항목.

## Gate C — knowledge graph (UA 후)

UA 미설치면 **SKIP** (실패가 아니라 보류). 설치 후:

- [ ] 입력 revision이 Gate B 통과본과 동일
- [ ] `.ua/knowledge-graph.json`의 `kind` = `knowledge`
- [ ] 노드 비어 있지 않고 ID 유일
- [ ] `edges` 양 끝점이 실제 노드에 존재 (dangling 없음)
- [ ] 분석 배치 완료, graph/meta freshness가 이번 실행 이후
- [ ] 그래프 가설을 canonical에 자동 반영하지 않음

**통과 조건:** 위 항목 또는 공식 SKIP 기록.
