# Finding Card (샘플)

## 메타
- ID: `FG-2026-04-14-006`
- 상태: `TRIAGE`
- 취약점 유형: `Misconfiguration (보안 헤더/오류응답)`
- 발견 일시: `2026-04-14 17:05 KST`
- 발견자: `tester-A`

## 대상
- 기능: 공통 API 게이트웨이
- Method/Endpoint: `GET /api/v1/profile`, `POST /api/v1/payment/create` (샘플)
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 재현 요약
1. 기준 요청(`MISC-HEADER-081`)으로 보안 헤더(`CSP`, `X-Frame-Options`, `Cache-Control`) 존재 여부를 확인합니다.
2. 오류 유도 요청(`MISC-ERROR-082`)으로 에러 응답의 내부 정보 노출 여부를 확인합니다.
3. CORS 점검 요청(`MISC-CORS-084`)으로 허용 원본 정책을 검토합니다.

## 전제조건
- 로그인 세션 필요
- 과도한 요청 없이 단건 점검 수행

## 실제 결과
- 응답 코드: `200/400`
- 응답 요약: 일부 엔드포인트에서 보안 헤더 누락과 오류 응답 상세 노출 정황 확인(샘플 시나리오)
- 화면 요약: 디버그성 식별자/내부 필드 일부 표시

## 기대 결과
- 공통 보안 헤더가 일관되게 적용되고, 오류 응답은 내부 구현 정보를 노출하지 않아야 함

## 영향도 평가
- 영향 범위: 전역 API 보안 정책
- 악용 난이도: 낮음~중간
- 비즈니스 임팩트: 공격 표면 확대, 정보 노출 가능성 증가
- 임시 우선순위: `P3`

## 증거
- 요청 파일: `evidence/2026-04-14/misc/reqres/1610_misc_header_check.txt`
- 응답 파일: `evidence/2026-04-14/misc/reqres/1611_misc_error_exposure.txt`
- 스크린샷: `evidence/2026-04-14/misc/screens/1613_misc_header_result.png`
- 로그 타임스탬프: `findings/2026-04-14_DAY7_LOG_KR.md`

## 비고
- 정책 준수 확인:
  - [x] User-Agent credential 고정
  - [x] SSRF는 `bugbounty.toss.sb`로만 검증
  - [x] 금액변조는 100원만 검증
  - [x] 과도한 요청/가용성 영향 없음
