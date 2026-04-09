# 취약점 제보서(폼 양식 맞춤) - SSRF 샘플

## 취약점 유형
SSRF

## 대상
https://tosscx.com

## 취약점 제목
URL 미리보기 기능에서 서버측 외부 요청 수행 가능성

## 공격 환경
웹 URL미리보기/계정A/Burp

## 공격 페이로드
`url=http://bugbounty.toss.sb`

## 취약점 설명 및 발생원인
URL 미리보기 API(`POST /api/v1/link/preview`)에 입력된 URL을 서버가 처리하는 과정에서 외부 요청 수행 정황이 확인되었습니다.  
검증은 정책에 맞게 `http://bugbounty.toss.sb`로만 진행했습니다.

재현 절차:
1. 정상 URL로 기준 요청(`URL-BASELINE-051`)을 전송합니다.
2. 동일 요청의 `url` 파라미터를 `http://bugbounty.toss.sb`로 변경해 단건 전송합니다(`URL-SSRF-052`).
3. 응답/로그를 비교해 서버측 요청 처리 정황을 확인합니다.

실제 결과:
- 검증 도메인 기준으로 서버측 외부 요청 수행 정황 확인.

기대 결과:
- 외부 요청이 필요한 기능이라도 목적지/스킴/리다이렉트 제한이 강제되어야 하며,
- 불필요한 외부 요청은 차단되어야 함.

발생원인 추정:
- URL 입력값 검증 및 목적지 제한(allowlist) 정책 미흡.

## 취약점 파급력
입력 URL 처리 로직이 내부 자원 대상으로 확장될 경우 정보 노출 또는 우회 접근 위험이 있습니다.  
특히 URL 처리 기능은 공통 컴포넌트로 재사용되는 경우 영향 범위가 넓어질 수 있습니다.

## 취약점 대응방안
목적지 allowlist, 사설대역/메타데이터 주소 차단, 리다이렉트 제한을 적용해야 합니다.  
또한 DNS 재검증 및 프로토콜 제한(예: http/https만 허용)을 적용해 우회 가능성을 줄여야 합니다.

## 첨부파일
- `evidence/2026-04-11/url_input/reqres/1311_url_preview_ssrf_probe.txt`
- `evidence/2026-04-11/url_input/reqres/1312_url_preview_compare.txt`
- `evidence/2026-04-11/url_input/screens/1313_url_preview_result.png`
- `findings/2026-04-11_DAY4_LOG_KR.md`
