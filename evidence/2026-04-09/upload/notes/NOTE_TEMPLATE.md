# 2026-04-09 / upload Notes

## Test Objective
- `fileId` 치환 기반 다운로드 접근통제 검증

## Request IDs
- `UPLOAD-IDOR-031` (기준)
- `UPLOAD-IDOR-032` (변조)

## Parameter Changes
- Download 요청의 `fileId`를 A 소유값으로 변경 후 B 세션 전송

## Observed Response
- Status: 기준 `200`, 변조 `404` (샘플)
- Key fields: `fileId`, `ownerId`, `signedUrl`

## Evidence Files
- reqres: `1150_file_download_baseline_A.txt`, `1151_file_download_idor_B.txt`
- screens: `1152_file_download_blocked_B.png`

## Signal Check
- [ ] Access control issue
- [ ] Input validation issue
- [ ] Data exposure issue

## Next Step
- 오류코드 정책(403 vs 404) 일관성 검증 1회 추가
