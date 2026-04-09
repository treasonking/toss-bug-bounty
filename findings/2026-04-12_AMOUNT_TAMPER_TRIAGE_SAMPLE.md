# Finding Card (샘플)

## 메타
- ID: `FG-2026-04-12-004`
- 상태: `TRIAGE`
- 취약점 유형: `Amount Tampering`
- 발견 일시: `2026-04-12 16:10 KST`
- 발견자: `tester-A`

## 대상
- 기능: 결제 생성/확정
- Method/Endpoint: `POST /api/v1/payment/create`, `POST /api/v1/payment/confirm`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 재현 요약
1. `amount=100` 정상 요청(`PAY-AMT-BASE-061`)을 전송합니다.
2. 동일 요청에서 `amount` 또는 `fee`만 단건 변조(`PAY-AMT-TAMPER-062`, `PAY-FEE-TAMPER-063`)합니다.
3. 생성-확정 단계 응답(`PAY-CONFIRM-CHECK-064`)을 비교해 서버 재검증 여부를 확인합니다.

## 전제조건
- 로그인 세션 필요
- 정책 준수: 100원 테스트만 수행

## 실제 결과
- 응답 코드: `200/400` 혼재
- 응답 요약: 일부 케이스에서 클라이언트 전달 금액이 반영되는 정황(샘플 시나리오)
- 화면 요약: 결제 확인 화면에서 변조값 반영 가능성 표시

## 기대 결과
- 서버는 클라이언트 금액을 신뢰하지 않고 주문 원본 기준으로 재계산/검증해야 함

## 영향도 평가
- 영향 범위: 결제 금액 무결성
- 악용 난이도: 중간
- 비즈니스 임팩트: 금전/정산 오류 가능성
- 임시 우선순위: `P1`

## 증거
- 요청 파일: `evidence/2026-04-12/payment/reqres/1411_payment_amount_tamper.txt`
- 응답 파일: `evidence/2026-04-12/payment/reqres/1413_payment_confirm_check.txt`
- 스크린샷: `evidence/2026-04-12/payment/screens/1414_payment_tamper_result.png`
- 로그 타임스탬프: `findings/2026-04-12_DAY5_LOG_KR.md`

## 비고
- 정책 준수 확인:
  - [x] User-Agent credential 고정
  - [x] SSRF는 `bugbounty.toss.sb`로만 검증
  - [x] 금액변조는 100원만 검증
  - [x] 과도한 요청/가용성 영향 없음
