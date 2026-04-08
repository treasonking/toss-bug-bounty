# Evidence 운영 규칙

## 디렉터리 구조
```text
evidence/
  YYYY-MM-DD/
    auth/
      reqres/
      screens/
      notes/
    profile/
      reqres/
      screens/
      notes/
    payment/
      reqres/
      screens/
      notes/
    upload/
      reqres/
      screens/
      notes/
    url_input/
      reqres/
      screens/
      notes/
```

## 파일명 규칙
- 요청/응답: `HHMM_<feature>_<action>_<account>.txt`
- 스크린샷: `HHMM_<feature>_<action>_<account>.png`
- 메모: `HHMM_<feature>_<action>_<account>.md`

예시:
- `1012_profile_read_baseline_A.txt`
- `1015_profile_read_idor_B.txt`
- `1016_profile_read_idor_B.png`

## 기록 최소 단위
- 변조 전 요청/응답 1쌍
- 변조 후 요청/응답 1쌍
- 결과 화면 1장
- 타임스탬프 포함 메모 1개

## 보안/정책 준수
- 민감정보 마스킹 후 저장
- 실제 사용자 데이터 저장 금지
- 외부 공유 금지
