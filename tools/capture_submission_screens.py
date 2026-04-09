#!/usr/bin/env python3
"""Capture Toss Bug Bounty report-form screenshots after manual login.

Usage:
  python tools/capture_submission_screens.py

Flow:
1) Chromium launches in visible mode.
2) User logs in and opens the "취약점 제보" form page manually.
3) Press Enter in terminal.
4) Script captures screenshots only when form markers are detected.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

FORM_MARKERS = [
    "text=취약점 제보",
    "text=취약점 유형",
    "text=공격 환경",
    "text=공격 페이로드",
]


def safe_wait_for_selector(page, selector: str, timeout_ms: int = 8000) -> bool:
    try:
        page.wait_for_selector(selector, timeout=timeout_ms)
        return True
    except PlaywrightTimeoutError:
        return False


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "evidence" / datetime.now().strftime("%Y-%m-%d") / "misc" / "screens"
    out_dir.mkdir(parents=True, exist_ok=True)

    user_data_dir = root / ".playwright-profile"
    user_data_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            headless=False,
            viewport={"width": 1600, "height": 1200},
        )
        page = context.new_page()
        page.goto("https://bugbounty.toss.im/", wait_until="domcontentloaded")

        print("[1/4] 브라우저가 열렸습니다. 로그인 후 '취약점 제보' 작성 페이지를 직접 여세요.")
        input("[2/4] 준비되면 여기서 Enter를 누르세요...")

        page.wait_for_timeout(800)
        found = sum(1 for marker in FORM_MARKERS if safe_wait_for_selector(page, marker, timeout_ms=2000))
        timestamp = datetime.now().strftime("%H%M%S")

        if found < 2:
            debug_path = out_dir / f"{timestamp}_debug_not_form.png"
            html_path = out_dir / f"{timestamp}_debug_not_form.html"
            page.screenshot(path=str(debug_path), full_page=True)
            html_path.write_text(page.content(), encoding="utf-8")
            print("[3/4] 제보 폼 마커를 찾지 못했습니다. 현재 페이지를 디버그로 저장했습니다.")
            print(f"       screenshot: {debug_path}")
            print(f"       html:       {html_path}")
            print("[4/4] 브라우저를 닫으려면 Enter를 누르세요.")
            input()
            context.close()
            return

        full_path = out_dir / f"{timestamp}_submission_write_full.png"
        viewport_path = out_dir / f"{timestamp}_submission_write_viewport.png"
        form_path = out_dir / f"{timestamp}_submission_write_form.png"

        page.screenshot(path=str(full_path), full_page=True)
        print(f"[3/4] Full screenshot saved: {full_path}")
        page.screenshot(path=str(viewport_path), full_page=False)
        print(f"[3/4] Viewport screenshot saved: {viewport_path}")

        form_locator = page.locator("form").first
        if form_locator.count() > 0:
            form_locator.screenshot(path=str(form_path))
            print(f"[3/4] Form screenshot saved: {form_path}")
        else:
            # Fallback: capture central area when form element is not explicit.
            page.locator("body").screenshot(path=str(form_path))
            print(f"[3/4] Form fallback screenshot saved: {form_path}")

        print("[4/4] 캡처 완료. 브라우저를 닫으려면 Enter를 누르세요.")
        input()
        context.close()


if __name__ == "__main__":
    main()
