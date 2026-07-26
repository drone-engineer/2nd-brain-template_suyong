# Hermes: llm-wiki-ains 스킬 분리

Hermes 번들에 `llm-wiki`가 이미 있어, vault 커스텀 스킬과 **이름이 같으면 충돌**한다.
ains-lab 멘토 권장: 커스텀 스킬을 **`llm-wiki-ains`**로 등록한다.

## 현재 구성 (이 머신)

| 항목 | 경로 / 값 |
| --- | --- |
| 스킬 본문 (vault) | `2nd_Brain_Template/.agents/skills/llm-wiki/` |
| SKILL.md `name` | `llm-wiki-ains` |
| Hermes 링크 | `~/.hermes/skills/custom/llm-wiki-ains` → vault 위 폴더 |
| 제거한 충돌 링크 | `~/.hermes/skills/llm-wiki` (삭제됨) |
| Cron `second-brain-collect-review` | Skills: `llm-wiki-ains` |
| Hermes 번들 (유지) | `~/.hermes/hermes-agent/skills/research/llm-wiki` |

## 재설치 시

```bash
VAULT="/Users/drone_engineer/cursor/Fulll-stack_B/2nd_Brain_Template/.agents/skills/llm-wiki"
mkdir -p ~/.hermes/skills/custom
rm -f ~/.hermes/skills/llm-wiki   # 이름 충돌 방지
ln -sfn "$VAULT" ~/.hermes/skills/custom/llm-wiki-ains
hermes cron edit 31830320217b --skill llm-wiki-ains
```

Cursor는 프로젝트 `.agents/skills/llm-wiki/` 경로로 계속 로드한다.  
Hermes/Telegram·Cron에서는 **`llm-wiki-ains`**를 선택한다.
