# 2026-04-09 / profile Notes

## Test Objective
- `userId` 치환 기반 IDOR/BOLA 단건 검증

## Request IDs
- `PROFILE-IDOR-011` (기준)
- `PROFILE-IDOR-012` (변조)

## Parameter Changes
- Path: `/profile/{userId}` 에서 `A12345 -> A12345(타세션 B)` 치환

## Observed Response
- Status: 기준 `200`, 변조 `200` (샘플 시나리오)
- Key fields: `userId`, `nickname`, `maskedPhone`

## Evidence Files
- reqres: `1110_profile_read_idor_B.txt`, `1111_profile_read_idor_resp_B.txt`
- screens: `1112_profile_idor_result_B.png`

## Signal Check
- [x] Access control issue
- [ ] Input validation issue
- [x] Data exposure issue

## Next Step
- finding 카드 `FG-2026-04-09-001`와 연계해 재현성 1회 추가 검증
