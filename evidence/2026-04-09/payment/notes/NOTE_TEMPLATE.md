# 2026-04-09 / payment Notes

## Test Objective
- `transactionId` 치환 기반 BOLA 단건 검증

## Request IDs
- `PAYMENT-BOLA-021` (기준)
- `PAYMENT-BOLA-022` (변조)

## Parameter Changes
- Query/Path의 `transactionId`를 A 소유값으로 고정 후 B 세션 재전송

## Observed Response
- Status: 기준 `200`, 변조 `403` (샘플)
- Key fields: `transactionId`, `amount`, `status`

## Evidence Files
- reqres: `1130_tx_detail_baseline_A.txt`, `1131_tx_detail_bola_B.txt`
- screens: `1132_tx_bola_blocked_B.png`

## Signal Check
- [ ] Access control issue
- [ ] Input validation issue
- [ ] Data exposure issue

## Next Step
- 다른 거래 엔드포인트 1건에서 동일 정책(403/404) 일관성 확인
