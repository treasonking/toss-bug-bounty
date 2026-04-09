# 2026-04-08 Evidence Summary

## Today Goals
- [x] User-Agent credential 고정 검증(로그인/조회/수정 3건)
- [x] 정상 플로우 기준선 요청/응답 수집
- [x] Day 2 교차검증 대상 API 3개 확정

## Completed Tests
- [x] 로그인 기준선 수집
  - Request ID(샘플): `AUTH-BASELINE-001`
  - Evidence: `evidence/2026-04-08/auth/reqres/1005_auth_login_baseline_A.txt`
- [x] 프로필 조회 기준선 수집
  - Request ID(샘플): `PROFILE-BASELINE-001`
  - Evidence: `evidence/2026-04-08/profile/reqres/1020_profile_read_baseline_A.txt`
- [x] 거래 조회 기준선 수집
  - Request ID(샘플): `PAYMENT-BASELINE-001`
  - Evidence: `evidence/2026-04-08/payment/reqres/1035_payment_history_baseline_A.txt`

## Candidate Findings
- `N/A` (Day 1은 기준선 수집 중심)

## Evidence Gaps
- [x] 응답 헤더 캡처 누락 여부 점검
- [ ] 스크린샷 타임스탬프 누락 여부 점검 (2건 보강 필요)

## Next Actions
- Day 2에서 A/B 계정 교차 요청으로 IDOR/BOLA 단건 검증
