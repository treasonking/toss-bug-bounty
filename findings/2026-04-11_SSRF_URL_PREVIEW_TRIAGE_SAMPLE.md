# Finding Card (샘플)

## 메타
- ID: `FG-2026-04-11-003`
- 상태: `TRIAGE`
- 취약점 유형: `SSRF 가능성`
- 발견 일시: `2026-04-11 14:50 KST`
- 발견자: `tester-A`

## 대상
- 기능: URL 미리보기
- Method/Endpoint: `POST /api/v1/link/preview`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 재현 요약
1. 정상 URL 요청(`URL-BASELINE-051`)을 전송해 기준 응답을 확인합니다.
2. `url=http://bugbounty.toss.sb` 요청(`URL-SSRF-052`)을 단건 전송합니다.
3. 응답/로그를 비교해 서버측 요청 정황을 확인합니다.

## 전제조건
- 로그인 세션 필요
- 안전 검증 규칙 준수(검증 도메인 한정)

## 실제 결과
- 응답 코드: `200`
- 응답 요약: 서버가 입력 URL 처리 중 외부 요청 수행 정황 확인(샘플 시나리오)
- 화면 요약: 미리보기 결과가 반환됨

## 기대 결과
- 정책상 허용된 경우에도 목적지 검증/제한 정책이 명확히 적용되어야 함

## 영향도 평가
- 영향 범위: 외부 URL 처리 로직
- 악용 난이도: 중간
- 비즈니스 임팩트: 내부자원 접근으로 확장될 잠재 위험
- 임시 우선순위: `P2`

## 증거
- 요청 파일: `evidence/2026-04-11/url_input/reqres/1311_url_preview_ssrf_probe.txt`
- 응답 파일: `evidence/2026-04-11/url_input/reqres/1312_url_preview_compare.txt`
- 스크린샷: `evidence/2026-04-11/url_input/screens/1313_url_preview_result.png`
- 로그 타임스탬프: `findings/2026-04-11_DAY4_LOG_KR.md`

## 비고
- 정책 준수 확인:
  - [x] User-Agent credential 고정
  - [x] SSRF는 `bugbounty.toss.sb`로만 검증
  - [x] 금액변조는 100원만 검증
  - [x] 과도한 요청/가용성 영향 없음
