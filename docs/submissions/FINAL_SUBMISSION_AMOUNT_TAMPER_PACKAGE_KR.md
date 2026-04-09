# 최종 제출 패키지 (완성본 샘플) - 금액변조

## 제목
[Amount Tampering] 결제 생성/확정 단계에서 금액 무결성 검증 미흡

## 취약점 유형
- Amount Tampering (비즈니스 로직 검증 미흡)

## 대상 URL/API
- Method: `POST`
- Endpoint: `/api/v1/payment/create`, `/api/v1/payment/confirm`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 공격 환경
- 테스트 일시: `2026-04-12 16:10 KST`
- 테스트 계정: A
- User-Agent(credential 고정): 적용 확인
- 프록시/Burp 사용 여부: 사용

## 전제조건
- 로그인 세션 필요
- 정책 준수: 100원 테스트만 수행

## 재현 절차
1. `amount=100` 정상 요청(`PAY-AMT-BASE-061`)을 전송해 기준 응답을 확보합니다.
2. 동일 요청에서 `amount` 또는 `fee` 한 필드만 변경해 전송합니다(`PAY-AMT-TAMPER-062`, `PAY-FEE-TAMPER-063`).
3. 생성/확정 단계 응답(`PAY-CONFIRM-CHECK-064`)을 비교해 서버 재검증 여부를 확인합니다.

## 실제 결과
- 일부 케이스에서 클라이언트 전달값이 처리 흐름에 반영되는 정황이 확인됩니다.

## 기대 결과
- 서버는 클라이언트 전달 금액을 신뢰하지 않고 주문 원본 기준으로 재계산/검증해야 합니다.

## 파급력
- 결제 금액 무결성 훼손 가능성
- 정산/수수료 계산 오류 가능성

## 발생 원인 추정
- 서버측 금액 재검증 로직 부재 또는 검증 순서 결함

## 대응방안
- 서버측 최종 금액 재계산 강제
- 생성/확정 단계 무결성 토큰 검증
- 금액/수수료 불일치 시 즉시 거절

## 증거 맵
- 요청/응답:
  - `evidence/2026-04-12/payment/reqres/1411_payment_amount_tamper.txt`
  - `evidence/2026-04-12/payment/reqres/1413_payment_confirm_check.txt`
- 스크린샷:
  - `evidence/2026-04-12/payment/screens/1414_payment_tamper_result.png`
- 실행 로그:
  - `findings/2026-04-12_DAY5_LOG_KR.md`
- 후보 카드:
  - `findings/2026-04-12_AMOUNT_TAMPER_TRIAGE_SAMPLE.md`

## 제출 전 체크
- [x] User-Agent credential 고정 사용
- [x] 100원 정책 준수
- [x] 자동화 대량 요청 미사용
- [x] 실제 피해 유발 동작 미수행
