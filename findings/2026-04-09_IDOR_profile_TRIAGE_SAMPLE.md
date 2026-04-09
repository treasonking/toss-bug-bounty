# Finding Card (샘플)

## 메타
- ID: `FG-2026-04-09-001`
- 상태: `TRIAGE`
- 취약점 유형: `IDOR/BOLA`
- 발견 일시: `2026-04-09 11:40 KST`
- 발견자: `tester-A`

## 대상
- 기능: 프로필 조회
- Method/Endpoint: `GET /api/v1/profile/{userId}`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 재현 요약
1. 계정 A로 `userId=A12345` 프로필 조회 요청을 캡처합니다.
2. 계정 B 세션에서 경로 변수만 `A12345`로 치환해 요청합니다.
3. 응답 코드/본문에 A 계정 정보가 포함되는지 확인합니다.

## 전제조건
- 계정 A/B 로그인 세션 필요
- 계정 A `userId` 식별 가능

## 실제 결과
- 응답 코드: `200`
- 응답 요약: 계정 B 요청에도 계정 A 프로필 필드 일부가 응답됨(샘플 시나리오)
- 화면 요약: 프로필 화면에 타계정 닉네임 표시 가능성 확인

## 기대 결과
- 타계정 `userId` 요청은 `403` 또는 `404`로 차단되어야 함

## 영향도 평가
- 영향 범위: 사용자 프로필 데이터 노출
- 악용 난이도: 낮음(식별자 확보 시)
- 비즈니스 임팩트: 개인정보 노출 및 신뢰도 저하
- 임시 우선순위: `P2`

## 증거
- 요청 파일: `evidence/2026-04-09/profile/reqres/1110_profile_read_idor_B.txt`
- 응답 파일: `evidence/2026-04-09/profile/reqres/1111_profile_read_idor_resp_B.txt`
- 스크린샷: `evidence/2026-04-09/profile/screens/1112_profile_idor_result_B.png`
- 로그 타임스탬프: `findings/2026-04-09_DAY2_LOG_KR.md`

## 비고
- 정책 준수 확인:
  - [x] User-Agent credential 고정
  - [x] SSRF는 `bugbounty.toss.sb`로만 검증
  - [x] 금액변조는 100원만 검증
  - [x] 과도한 요청/가용성 영향 없음
