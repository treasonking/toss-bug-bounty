# Finding Card (샘플)

## 메타
- ID: `FG-2026-04-10-002`
- 상태: `TRIAGE`
- 취약점 유형: `BOLA`
- 발견 일시: `2026-04-10 15:20 KST`
- 발견자: `tester-A`

## 대상
- 기능: 파일 메타 조회
- Method/Endpoint: `GET /api/v1/files/{fileId}/meta`
- 앱/웹 버전: `모바일 앱 vX.Y.Z`

## 재현 요약
1. 계정 A로 파일 업로드 후 `fileId=F8891`를 확보합니다.
2. 계정 B 세션으로 `/files/F8891/meta` 요청을 보냅니다.
3. 응답에 A 소유 파일 메타(`ownerId`, `filename`)가 포함되는지 확인합니다.

## 전제조건
- 계정 A/B 로그인 필요
- A 업로드 파일 식별자 확보 필요

## 실제 결과
- 응답 코드: `200`
- 응답 요약: B 세션으로 A 파일 메타 일부가 노출됨(샘플 시나리오)
- 화면 요약: 파일 상세 화면에서 타계정 파일명 확인 가능

## 기대 결과
- 비소유 계정 요청은 `403/404`로 차단되어야 함

## 영향도 평가
- 영향 범위: 파일 메타(파일명/소유자/업로드시각) 노출
- 악용 난이도: 중간(식별자 확보 필요)
- 비즈니스 임팩트: 내부 문서명/개인정보 추론 가능성
- 임시 우선순위: `P2`

## 증거
- 요청 파일: `evidence/2026-04-10/upload/reqres/1230_file_meta_bola_B.txt`
- 응답 파일: `evidence/2026-04-10/upload/reqres/1231_file_meta_bola_resp_B.txt`
- 스크린샷: `evidence/2026-04-10/upload/screens/1232_file_meta_bola_B.png`
- 로그 타임스탬프: `findings/2026-04-10_DAY3_LOG_KR.md`

## 비고
- 정책 준수 확인:
  - [x] User-Agent credential 고정
  - [x] SSRF는 `bugbounty.toss.sb`로만 검증
  - [x] 금액변조는 100원만 검증
  - [x] 과도한 요청/가용성 영향 없음
