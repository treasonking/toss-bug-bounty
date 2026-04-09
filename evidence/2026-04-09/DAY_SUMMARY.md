# 2026-04-09 Evidence Summary

## Today Goals
- [ ] 프로필/거래/파일의 IDOR/BOLA 단건 검증
- [ ] A/B 계정 요청 차이표 작성
- [ ] 재현 가능한 후보 1건 카드화

## Completed Tests
- [ ] 프로필 userId 치환 테스트
- [ ] 거래 transactionId 치환 테스트
- [ ] 파일 fileId 교차 접근 테스트

## Candidate Findings
- [ ] 200 응답 기반 타계정 데이터 노출 여부

## Evidence Gaps
- [ ] 변조 전후 요청 쌍 누락 여부
- [ ] 권한 오류코드(403/404) 비교 기록 누락 여부

## Next Actions
- Day 3 파일 접근통제/서명 URL 검증 심화
