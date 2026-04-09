# 2026-04-10 / upload Notes

## Test Objective
- 파일 업/다운로드 접근통제 및 서명 URL 만료 정책 검증

## Request IDs
- `UPLOAD-BASELINE-041` (업로드 기준)
- `UPLOAD-ACCESS-042` (타세션 다운로드)
- `UPLOAD-SIGNEDURL-043` (만료 전후 비교)

## Parameter Changes
- `fileId`를 A 소유값으로 고정 후 B 세션 재전송
- `signedUrl` 만료 시점 전/후 동일 URL 재호출

## Observed Response
- Status: 업로드 `201`, 교차 다운로드 `404`, 만료 후 `403` (샘플)
- Key fields: `fileId`, `ownerId`, `signedUrl`, `expiresAt`

## Evidence Files
- reqres: `1210_upload_baseline_A.txt`, `1211_upload_access_B.txt`, `1212_upload_signedurl_expiry.txt`
- screens: `1213_upload_download_blocked_B.png`

## Signal Check
- [ ] Access control issue
- [ ] Input validation issue
- [ ] Data exposure issue

## Next Step
- 파일 메타 조회 API 1건에서 `ownerId` 검증 일관성 재확인
