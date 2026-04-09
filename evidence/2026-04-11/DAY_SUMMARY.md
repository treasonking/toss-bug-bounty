# 2026-04-11 Evidence Summary

## Today Goals
- [x] URL 입력 기능 SSRF 가능성 안전 검증
- [x] bugbounty.toss.sb 단일 도메인으로 증적 수집
- [x] 정책 일관성(허용/차단) 확인

## Completed Tests
- [x] 정상 URL 미리보기 기준선
  - Request ID(샘플): `URL-BASELINE-051`
- [x] 검증용 도메인 입력 테스트
  - Request ID(샘플): `URL-SSRF-052`
- [x] 일반 URL 대비 응답 비교
  - Request ID(샘플): `URL-COMPARE-053`

## Candidate Findings
- [x] 서버측 외부 요청 수행 정황 (검증 도메인 한정 샘플)

## Evidence Gaps
- [x] 요청 바디 URL 파라미터 캡처 누락 여부
- [ ] 응답 본문/상태코드 비교표 누락 여부 (1건 보강)

## Next Actions
- Day 5 100원 금액변조 검증
