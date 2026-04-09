# 2026-04-08 / auth Notes

## Test Objective
- User-Agent credential 고정 적용 여부와 로그인 응답 기준선 확인

## Request IDs
- `AUTH-BASELINE-001`

## Parameter Changes
- 없음(기준선 수집)

## Observed Response
- Status: `200`
- Key fields: `accessToken`, `refreshToken`, `expiresIn`

## Evidence Files
- reqres: `1005_auth_login_baseline_A.txt`
- screens: `1006_auth_login_success_A.png`

## Signal Check
- [ ] Access control issue
- [ ] Input validation issue
- [ ] Data exposure issue

## Next Step
- Day 2에서 B 세션으로 보호 API 접근 차단 여부 확인
