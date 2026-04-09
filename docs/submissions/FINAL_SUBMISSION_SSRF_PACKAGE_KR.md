# 최종 제출 패키지 (완성본 샘플) - SSRF

## 제목
[SSRF] URL 미리보기 기능에서 서버측 외부 요청 수행 가능

## 취약점 유형
- SSRF 가능성

## 대상 URL/API
- Method: `POST`
- Endpoint: `/api/v1/link/preview`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 공격 환경
- 테스트 일시: `2026-04-11 14:50 KST`
- 테스트 계정: A
- User-Agent(credential 고정): 적용 확인
- 프록시/Burp 사용 여부: 사용

## 전제조건
- 로그인 세션 필요
- 안전 검증 규칙 준수(`http://bugbounty.toss.sb` 한정)

## 재현 절차
1. 정상 URL 요청(`URL-BASELINE-051`)으로 기준 응답을 확보합니다.
2. 동일 요청의 `url` 파라미터를 `http://bugbounty.toss.sb`로 변경해 단건 전송합니다.
3. 응답/로그를 비교해 서버측 요청 처리 정황을 확인합니다.

## 실제 결과
- 검증 도메인 기준으로 서버측 외부 요청 수행 정황이 확인됩니다.

## 기대 결과
- 외부 요청이 필요한 기능이라면 허용 대상/스킴/리다이렉트 정책을 엄격히 제한해야 하며,
- 불필요한 외부 요청은 차단되어야 합니다.

## 파급력
- 내부 자원 대상으로 요청이 확장될 경우 정보 노출/접근 우회 가능성

## 발생 원인 추정
- URL 입력값 검증/목적지 제한 정책 부족

## 대응방안
- 목적지 allowlist 적용
- 사설대역/메타데이터 주소 차단
- 리다이렉트/프로토콜 제한 및 재검증

## 증거 맵
- 요청/응답:
  - `evidence/2026-04-11/url_input/reqres/1311_url_preview_ssrf_probe.txt`
  - `evidence/2026-04-11/url_input/reqres/1312_url_preview_compare.txt`
- 스크린샷:
  - `evidence/2026-04-11/url_input/screens/1313_url_preview_result.png`
- 실행 로그:
  - `findings/2026-04-11_DAY4_LOG_KR.md`
- 후보 카드:
  - `findings/2026-04-11_SSRF_URL_PREVIEW_TRIAGE_SAMPLE.md`

## 제출 전 체크
- [x] User-Agent credential 고정 사용
- [x] SSRF 검증 도메인 정책 준수(`bugbounty.toss.sb`)
- [x] 자동화 대량 요청 미사용
- [x] 실제 피해 유발 동작 미수행
