# 2026-04-11 / url_input Notes

## Test Objective
- URL 입력 기능의 서버측 요청 수행 여부를 안전 범위 내에서 확인

## Request IDs
- `URL-BASELINE-051` (정상 URL)
- `URL-SSRF-052` (검증용 도메인)
- `URL-COMPARE-053` (비교 요청)

## Parameter Changes
- `url` 파라미터만 변경
- 검증 도메인: `http://bugbounty.toss.sb` 한정

## Observed Response
- Status: `200` (샘플)
- Key fields: `url`, `previewTitle`, `fetchedAt`, `status`

## Evidence Files
- reqres: `1310_url_preview_baseline.txt`, `1311_url_preview_ssrf_probe.txt`, `1312_url_preview_compare.txt`
- screens: `1313_url_preview_result.png`

## Signal Check
- [ ] Access control issue
- [ ] Input validation issue
- [ ] Data exposure issue

## Next Step
- Day 5 금액변조 테스트 전 응답 비교표(상태코드/본문길이) 1회 보강
