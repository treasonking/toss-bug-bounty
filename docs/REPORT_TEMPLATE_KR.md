# 버그바운티 제보 템플릿 (제보 폼 양식 기준)

## 취약점 유형
- (드롭다운 값 중 선택)

## 대상
- (아래 값 중 하나만 입력)
- `https://tossbank.com`
- `https://tosscx.com`
- `https://corp.tossinvest.com`
- `https://www.tosspayments.com`
- `https://tossinsu.com`
- `https://tossplace.com`
- `*.toss.im`
- `모바일 앱(안드로이드)`
- `모바일 앱(iOS)`

## 취약점 제목
- 

## 공격 환경
- (아주 짧게 한 줄, 30자 내외 권장)
- 예: `웹 URL미리보기/계정A/Burp`
- 예: `모바일앱/계정A,B/Burp`

## 공격 페이로드
- (요청에서 실제로 변경/주입한 값, 최대 500자)
- 여러 줄로 작성 가능:
  - `url=http://bugbounty.toss.sb`
  - `GET /api/v1/profile/A12345` (B 세션)
  - `amount=100 -> amount=10`, `fee=0`

## 취약점 설명 및 발생원인
1. 재현 절차 1
2. 재현 절차 2
3. 재현 절차 3

- 실제 결과:
- 기대 결과:
- 발생원인 추정:

## 취약점 파급력
- 영향 범위:
- 악용 시나리오:
- 비즈니스 영향:

## 취약점 대응방안
- 서버 검증/권한 검증/입력 검증 보완안:
- 운영/모니터링 보완안:

## 첨부파일
- 요청/응답 파일:
- 스크린샷:
- 로그 타임스탬프:
