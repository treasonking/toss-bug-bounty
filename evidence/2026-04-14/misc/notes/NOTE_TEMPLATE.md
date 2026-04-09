# 2026-04-14 / misc Notes

## Test Objective
- 공통 보안 헤더/CORS/오류응답 설정의 Misconfiguration 여부 확인

## Request IDs
- `MISC-HEADER-081`
- `MISC-ERROR-082`
- `MISC-REPORT-083`

## Parameter Changes
- 오류 유도용 최소 파라미터 누락 요청 1건
- CORS/헤더 점검용 기준 요청 2건

## Observed Response
- Status: `200/400` (샘플)
- Key fields: `CSP`, `X-Frame-Options`, `Cache-Control`, `Access-Control-Allow-Origin`, `errorCode`

## Evidence Files
- reqres: `1610_misc_header_check.txt`, `1611_misc_error_exposure.txt`, `1612_misc_cors_check.txt`
- screens: `1613_misc_header_result.png`

## Signal Check
- [ ] Access control issue
- [x] Input validation issue
- [x] Data exposure issue

## Next Step
- 보고서에서 누락 헤더 목록과 권장 보안 설정을 명시
