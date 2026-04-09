# 2026-04-12 / payment Notes

## Test Objective
- 100원 기준 결제/송금 요청에서 서버 금액 무결성 검증 여부 확인

## Request IDs
- `PAY-AMT-BASE-061` (기준선)
- `PAY-AMT-TAMPER-062` (amount 변조)
- `PAY-FEE-TAMPER-063` (fee 변조)
- `PAY-CONFIRM-CHECK-064` (확정 단계)

## Parameter Changes
- `amount=100` 기준 요청 후 단일 필드 변조
- `fee`만 변경한 요청과 `amount`만 변경한 요청을 분리 비교

## Observed Response
- Status: 기준 `200`, 변조 케이스 `200/400` 혼재(샘플)
- Key fields: `amount`, `fee`, `serverCalculatedAmount`, `orderId`, `status`

## Evidence Files
- reqres: `1410_payment_amount_base_100.txt`, `1411_payment_amount_tamper.txt`, `1412_payment_fee_tamper.txt`, `1413_payment_confirm_check.txt`
- screens: `1414_payment_tamper_result.png`

## Signal Check
- [ ] Access control issue
- [x] Input validation issue
- [ ] Data exposure issue

## Next Step
- 보고서에 100원 정책 준수 사실과 서버 재검증 기대 동작 명시
