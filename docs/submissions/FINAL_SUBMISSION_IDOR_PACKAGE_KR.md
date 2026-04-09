# 최종 제출 패키지 (완성본 샘플) - IDOR/BOLA

## 제목
[IDOR/BOLA] 프로필 조회 API에서 타 사용자 정보 조회 가능

## 취약점 유형
- IDOR/BOLA (Broken Object Level Authorization)

## 대상 URL/API
- Method: `GET`
- Endpoint: `/api/v1/profile/{userId}`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 공격 환경
- 테스트 일시: `2026-04-09 11:40 KST`
- 테스트 계정: A(리소스 소유), B(비소유)
- User-Agent(credential 고정): 적용 확인
- 프록시/Burp 사용 여부: 사용

## 전제조건
- 계정 A/B 로그인 세션 필요
- 계정 A `userId` 식별 가능

## 재현 절차
1. 계정 A로 `GET /api/v1/profile/{userId}` 요청을 전송하여 `userId=A12345`를 확인합니다.
2. 계정 B 세션으로 동일 요청을 구성하고 경로 변수만 `A12345`로 설정합니다.
3. 응답 코드와 본문 필드(`nickname`, `maskedPhone`)를 비교합니다.

## 실제 결과
- 계정 B 요청임에도 `200` 응답과 함께 계정 A 프로필 필드 일부가 반환됩니다.

## 기대 결과
- 비소유 계정 요청은 `403` 또는 `404`로 차단되어야 하며 타사용자 정보가 반환되지 않아야 합니다.

## 파급력
- 사용자 프로필 정보 노출 가능
- 식별자 예측/유출과 결합 시 다수 사용자 정보 접근 위험

## 발생 원인 추정
- 서버가 인증 여부는 확인하지만 요청 사용자와 리소스 소유자 매핑 검증을 강제하지 않음

## 대응방안
- 객체 조회 시 `요청 사용자 == 리소스 소유자` 검증 강제
- 권한 실패 응답 정책(403/404) 일관화
- 주요 조회 API에 객체 수준 권한 테스트 케이스 추가

## 증거 맵
- 요청/응답:
  - `evidence/2026-04-09/profile/reqres/1110_profile_read_idor_B.txt`
  - `evidence/2026-04-09/profile/reqres/1111_profile_read_idor_resp_B.txt`
- 스크린샷:
  - `evidence/2026-04-09/profile/screens/1112_profile_idor_result_B.png`
- 실행 로그:
  - `findings/2026-04-09_DAY2_LOG_KR.md`
- 후보 카드:
  - `findings/2026-04-09_IDOR_profile_TRIAGE_SAMPLE.md`

## 제출 전 체크
- [x] User-Agent credential 고정 사용
- [x] 자동화 대량 요청 미사용
- [x] 실제 피해 유발 동작 미수행
- [x] 재현 절차 3단계 이상 명시
- [x] 실제 결과/기대 결과 명확히 구분
