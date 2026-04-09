# 제보 화면 자동 캡처 가이드

## 목적
로그인 이후 제보 화면을 자동으로 캡처해 첨부파일로 바로 사용할 수 있게 합니다.

## 준비
1. Python 설치 확인
2. Playwright 설치

```powershell
python -m pip install playwright
python -m playwright install chromium
```

## 실행
```powershell
python tools/capture_submission_screens.py
```

## 동작 방식
1. 브라우저가 열리면 직접 로그인합니다.
2. 제보 페이지 접근이 가능한 상태에서 터미널 Enter를 누릅니다.
3. 전체 화면 + 폼 영역 캡처가 자동 저장됩니다.

## 저장 위치
- `evidence/YYYY-MM-DD/misc/screens/`
- 파일명 예시:
  - `HHMMSS_01_submission_main_full.png`
  - `HHMMSS_02_submission_write_form.png`

## 참고
- 로그인은 수동으로 해야 합니다.
- 같은 프로필(`.playwright-profile`)을 재사용해서 다음 실행 시 로그인 유지 가능성이 높습니다.
