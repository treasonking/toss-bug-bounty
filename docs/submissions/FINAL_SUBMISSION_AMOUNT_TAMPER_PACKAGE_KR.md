# 취약점 제보서(폼 양식 맞춤) - 금액변조 샘플

## 취약점 유형
기타

## 대상
https://www.tosspayments.com

## 취약점 제목
결제 생성/확정 단계 금액 무결성 검증 미흡 가능성

## 공격 환경
결제 API / 계정 A / Burp Repeater / UA credential 고정 / 2026-04-12 16:10 KST / 100원 정책 준수

## 공격 페이로드
`amount=100 -> amount=10` 또는 `fee=0` (단건 변조 비교)

## 취약점 설명 및 발생원인
결제 생성/확정 API에서 클라이언트 전달 `amount`/`fee` 값에 대한 서버 재검증이 약해 보이는 정황이 확인되었습니다.

재현 절차:
1. `amount=100` 정상 요청(`PAY-AMT-BASE-061`)으로 기준 응답을 확보합니다.
2. 동일 요청에서 `amount` 또는 `fee` 한 필드만 변경해 전송합니다(`PAY-AMT-TAMPER-062`, `PAY-FEE-TAMPER-063`).
3. 생성/확정 단계 응답(`PAY-CONFIRM-CHECK-064`)을 비교하여 서버 재검증 여부를 확인합니다.

실제 결과:
- 일부 케이스에서 클라이언트 전달값이 처리 흐름에 반영되는 정황이 관찰됨(샘플 시나리오).

기대 결과:
- 서버는 클라이언트 전달 금액을 신뢰하지 않고 주문 원본 기준으로 재계산/검증해야 함.

발생원인 추정:
- 서버단 금액 재검증 로직 누락 또는 검증 순서 결함.

## 취약점 파급력
금액 무결성 훼손 시 결제/정산 정확성에 영향이 발생할 수 있으며, 비즈니스 로직 악용 가능성이 생길 수 있습니다.  
금융 서비스 특성상 신뢰도 저하 및 재무적 리스크로 이어질 수 있습니다.

## 취약점 대응방안
서버측 최종 금액 재계산을 강제하고, 생성/확정 단계 간 무결성 토큰 검증을 적용해야 합니다.  
`amount`, `fee`, `currency` 불일치 시 트랜잭션을 즉시 거절하고 감사 로그를 남겨야 합니다.

## 첨부파일
- `evidence/2026-04-12/payment/reqres/1411_payment_amount_tamper.txt`
- `evidence/2026-04-12/payment/reqres/1413_payment_confirm_check.txt`
- `evidence/2026-04-12/payment/screens/1414_payment_tamper_result.png`
- `findings/2026-04-12_DAY5_LOG_KR.md`
