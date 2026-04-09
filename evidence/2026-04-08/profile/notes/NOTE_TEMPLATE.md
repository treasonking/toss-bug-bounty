# 2026-04-08 / profile Notes

## Test Objective
- 프로필 조회 API 기준선 수집 및 식별자 위치 확인(`userId`)

## Request IDs
- `PROFILE-BASELINE-001`

## Parameter Changes
- 없음(기준선 수집)

## Observed Response
- Status: `200`
- Key fields: `userId`, `nickname`, `maskedPhone`

## Evidence Files
- reqres: `1020_profile_read_baseline_A.txt`
- screens: `1021_profile_screen_A.png`

## Signal Check
- [ ] Access control issue
- [ ] Input validation issue
- [ ] Data exposure issue

## Next Step
- Day 2에 B 세션으로 `userId` 교차 요청 단건 검증
