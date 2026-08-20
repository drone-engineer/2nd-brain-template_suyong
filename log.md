## [2026-08-20] compile | CBF 탈중앙 군집 항법·결속 유지

- 신규: `concepts/cbf-decentralized-swarm-connectivity.md`
- sources:
  - `raw/articles/2023-control-barrier-function-based-decentralized-uav-swarm-navigation-while-preservi.md`
  - `raw/articles/2024-connectivity-preserving-decentralized-uav-swarm-navigation-in-obstacle-laden-env.md`
- 링크: [[uav-formation-control]], [[uav-swarm-path-planning]], [[uav-swarm-robotics]], [[gnss-denied-autonomous-navigation]], [[combat-swarm-drone-operations]]
- index.md total 25 → 26; formation/path-planning 페이지에 역링크 추가
- note: demo compile for human (review-queue ① CBF Navigation)


- Fixed sha256 hash to match the exact byte content of the post-frontmatter body.
- The script bug was that compute_sha256() added an extra trailing '\n' for hashing but the files never wrote it.

## [2026-08-17] repair | SHA256 mismatch (fixed) in raw/articles/2026-08-17-ros2-drone-github-data.md

- Fixed sha256 hash to match the exact byte content of the post-frontmatter body.
- The script bug was that compute_sha256() added an extra trailing '\n' for hashing but the files never wrote it.

## [2026-08-17] update | daily-collect-generic.py

- Patched compute_sha256() to not add a trailing newline before hashing since write_raw_file() doesn't write one.
- Fixes future hash mismatches in cron jobs that would otherwise silently fail.

## [2026-08-21] ingest | ROS2 드론 기술 일일 수집 (GitHub API + PX4/ArduPilot 릴리즈 + PX4/ROS2 공식 문서)

- 새로운 raw 수집 파일:
  - `raw/articles/2026-08-21-ros2-drone-github-data.md` (SHA256: 77b4be5af2f162b6...)
  - `raw/articles/2026-08-21-px4-release-notes.md` (SHA256: c38b911f1344b76c...)
  - `raw/articles/2026-08-21-ardupilot-release-notes.md` (SHA256: 546488dfd205527a...)
  - `raw/articles/2026-08-21-px4-docs.md` (SHA256: b3c066c7c6c79ff9...)
  - `raw/articles/2026-08-21-ros2-docs.md` (SHA256: 63703450747fbd8b...)
- 보고서: `docs/reports/2026-08-21-ros2-drone-tech-report.md`
- 검증 메타데이터: `docs/workflow/2026-08-21-sha256-verification.json`, `docs/workflow/2026-08-21-github-data-summary.json`, `docs/workflow/2026-08-21-collect-results.json`
- Gate B 검증: 5개 파일 모두 SHA256 일치 ✅ (verify_sha256.py 기준)
- ROS2 docs: Anubis anti-bot으로 일부 페이지 수집 실패 (404/차단), 재수집 필요
- PX4 v1.18.0-beta2 (2026-08-09) 릴리즈 노트, ArduPilot 4.7.0 (2026-07-27) 릴리즈 노트 수집
- GitHub 수집 통계: 9 쿼리, 77개 중복 제거된 저장소
- 주요 동향: PX4 ⭐12456 (+7), JacopoPan/aerial-autonomy-stack ⭐573 (+1), Zenoh 9개 저장소 언급, YOLO 15개 저장소 언급