# SSRF 증거 자동 수집 (코드 분석 없이)

## 설치(최초 1회)
```powershell
python -m pip install playwright
python -m playwright install chromium
```

## 실행
```powershell
python tools/capture_ssrf_evidence.py
```

## 사용 방법
1. 브라우저가 열리면 로그인
2. Enter (before 캡처)
3. 앱에서 SSRF 재현 동작 1회 수행
4. Enter (after 캡처 + req/res 저장)

## 저장 위치
- `evidence/YYYY-MM-DD/url_input/reqres/`
- `evidence/YYYY-MM-DD/url_input/screens/`
- `evidence/YYYY-MM-DD/url_input/notes/*_ssrf_capture_summary.md`

## 수집되는 것
- 전체화면 before/after 스크린샷
- SSRF 관련 요청/응답 raw 텍스트
- 자동 요약 파일

## 기본 탐지 키워드
- `bugbounty.toss.sb`
- `/link/preview`
- `/preview`
- `/webhook`

필요하면 `tools/capture_ssrf_evidence.py` 상단 `TARGET_HOST_HINTS`만 수정하면 됩니다.
