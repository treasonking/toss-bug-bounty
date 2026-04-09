# 2026-04-09 Evidence Summary

## Today Goals
- [x] 프로필/거래/파일의 IDOR/BOLA 단건 검증
- [x] A/B 계정 요청 차이표 작성
- [x] 재현 가능한 후보 1건 카드화

## Completed Tests
- [x] 프로필 userId 치환 테스트
  - Request IDs(샘플): `PROFILE-IDOR-011`, `PROFILE-IDOR-012`
- [x] 거래 transactionId 치환 테스트
  - Request IDs(샘플): `PAYMENT-BOLA-021`, `PAYMENT-BOLA-022`
- [x] 파일 fileId 교차 접근 테스트
  - Request IDs(샘플): `UPLOAD-IDOR-031`, `UPLOAD-IDOR-032`

## Candidate Findings
- [x] 200 응답 기반 타계정 데이터 노출 여부 (프로필 API 샘플 시나리오)

## Evidence Gaps
- [x] 변조 전후 요청 쌍 누락 여부
- [ ] 권한 오류코드(403/404) 비교 기록 누락 여부 (파일 API 1건 보강)

## Next Actions
- Day 3 파일 접근통제/서명 URL 검증 심화
