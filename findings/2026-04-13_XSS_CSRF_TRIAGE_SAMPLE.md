# Finding Card (샘플)

## 메타
- ID: `FG-2026-04-13-005`
- 상태: `TRIAGE`
- 취약점 유형: `Stored/Reflected XSS + CSRF 보호 미흡 정황`
- 발견 일시: `2026-04-13 13:40 KST`
- 발견자: `tester-A`

## 대상
- 기능: 문의/알림/초대 상태변경
- Method/Endpoint: `POST /api/v1/support/message`, `POST /api/v1/notification/read`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 재현 요약
1. 문의 입력 필드에 무해 테스트 문자열을 전송(`CS-XSS-CHECK-071`)합니다.
2. 조회 시 출력 인코딩 적용 여부와 반사 표시를 확인합니다.
3. 상태변경 요청에서 토큰/Origin/Referer 조합(`CS-CSRF-CHECK-073`)을 비교합니다.

## 전제조건
- 로그인 세션 필요
- 무해 테스트 페이로드만 사용

## 실제 결과
- 응답 코드: `200/403` 혼재
- 응답 요약: 일부 입력 필드 인코딩 미흡 정황과 CSRF 검증 약한 요청 확인(샘플 시나리오)
- 화면 요약: 메시지 렌더링 시 반사 표시 가능성

## 기대 결과
- 입력값은 저장/출력 시 안전하게 인코딩되어야 하며, 상태변경 요청은 CSRF 방어를 강제해야 함

## 영향도 평가
- 영향 범위: 사용자 입력/상태변경 API
- 악용 난이도: 중간
- 비즈니스 임팩트: 세션 기반 행위 위임/XSS 악용 가능성
- 임시 우선순위: `P2`

## 증거
- 요청 파일: `evidence/2026-04-13/cs/reqres/1510_cs_xss_probe.txt`
- 응답 파일: `evidence/2026-04-13/cs/reqres/1512_cs_csrf_check.txt`
- 스크린샷: `evidence/2026-04-13/cs/screens/1513_cs_render_result.png`
- 로그 타임스탬프: `findings/2026-04-13_DAY6_LOG_KR.md`

## 비고
- 정책 준수 확인:
  - [x] User-Agent credential 고정
  - [x] SSRF는 `bugbounty.toss.sb`로만 검증
  - [x] 금액변조는 100원만 검증
  - [x] 과도한 요청/가용성 영향 없음
