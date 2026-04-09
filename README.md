# toss-bug-bounty

토스 버그바운티 실무 운영을 위한 한국어 문서/템플릿 모음입니다.

## 문서 구성
- `TOSS_BUG_BOUNTY_RUNBOOK_KR.md`: 전체 실행 런북
- `docs/CHECKLIST_KR.md`: 기능별 테스트 체크리스트
- `docs/REPORT_TEMPLATE_KR.md`: 제보 보고서 템플릿
- `docs/DAILY_LOG_TEMPLATE_KR.md`: 일일 테스트 로그 템플릿
- `docs/POC_PLAYBOOK_KR.md`: 취약점 유형별 안전 검증 PoC 플레이북
- `docs/samples/`: 제출 직전 참고용 샘플 제보서
- `findings/README.md`: 이슈 트래킹 운영 규칙
- `findings/2026-04-08_DAY1_LOG_KR.md`: Day 1 실행 로그 초안
- `findings/2026-04-09_DAY2_LOG_KR.md`: Day 2 실행 로그 초안
- `findings/2026-04-09_IDOR_profile_TRIAGE_SAMPLE.md`: Day 2 기반 샘플 finding 카드
- `findings/2026-04-10_FILE_META_BOLA_TRIAGE_SAMPLE.md`: Day 3 기반 샘플 finding 카드
- `findings/2026-04-10_DAY3_LOG_KR.md`: Day 3 실행 로그 초안
- `findings/2026-04-11_DAY4_LOG_KR.md`: Day 4 실행 로그 초안
- `findings/2026-04-12_DAY5_LOG_KR.md`: Day 5 실행 로그 초안
- `findings/2026-04-13_DAY6_LOG_KR.md`: Day 6 실행 로그 초안
- `findings/2026-04-14_DAY7_LOG_KR.md`: Day 7 실행 로그 초안
- `findings/FINDING_CARD_TEMPLATE_KR.md`: 취약점 카드 템플릿
- `evidence/README.md`: 증거 폴더 구조/파일명 규칙
- `evidence/DAY1_DAY7_STRUCTURE_KR.md`: Day1~Day7 실폴더 구성 안내
- `evidence/*/DAY_SUMMARY.md`: 날짜별 요약 템플릿
- `evidence/*/*/notes/NOTE_TEMPLATE.md`: 기능별 메모 템플릿

## 빠른 시작
1. `TOSS_BUG_BOUNTY_RUNBOOK_KR.md`의 `0) 전제와 운영 원칙`부터 확인
2. Burp에서 `User-Agent credential` 고정 규칙 적용
3. `docs/CHECKLIST_KR.md`로 기능별 수동 검증 수행
4. 발견 이슈는 `docs/REPORT_TEMPLATE_KR.md`로 즉시 정리
5. 후보 이슈는 `findings/FINDING_CARD_TEMPLATE_KR.md`로 카드화해 우선순위 관리
6. 제출 직전에는 `docs/samples/`로 문장/구조 최종 점검

## 운영 원칙 요약
- 실제 피해 유발 금지, 가능성만 안전하게 증명
- SSRF는 `http://bugbounty.toss.sb`로만 검증
- 금액변조는 100원으로만 검증
- 과도한 자동화/스캐닝/부하 유발 금지
- 취득 정보 비밀 유지
