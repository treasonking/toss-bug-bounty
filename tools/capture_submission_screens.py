#!/usr/bin/env python3
"""
Capture Toss Bug Bounty submission-page screenshots after manual login.

Usage:
  python tools/capture_submission_screens.py

Flow:
1) Chromium launches in visible mode.
2) User logs in manually.
3) Press Enter in terminal.
4) Script captures full-page screenshots and key form-area screenshots.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


@dataclass
class CaptureTarget:
    name: str
    url: str
    form_selector: str = "form"


TARGETS: List[CaptureTarget] = [
    CaptureTarget(
        name="submission_main",
        url="https://bugbounty.toss.im/",
    ),
    CaptureTarget(
        name="submission_write",
        url="https://bugbounty.toss.im/reports/new",
    ),
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

        print("[1/4] 브라우저가 열렸습니다. 로그인 후 제보 페이지까지 접근하세요.")
        input("[2/4] 준비되면 여기서 Enter를 누르세요...")

        for idx, target in enumerate(TARGETS, start=1):
            page.goto(target.url, wait_until="domcontentloaded")
            page.wait_for_timeout(1500)

            timestamp = datetime.now().strftime("%H%M%S")
            full_path = out_dir / f"{timestamp}_{idx:02d}_{target.name}_full.png"
            page.screenshot(path=str(full_path), full_page=True)
            print(f"[3/4] Full screenshot saved: {full_path}")

            if safe_wait_for_selector(page, target.form_selector):
                form = page.locator(target.form_selector).first
                clip_path = out_dir / f"{timestamp}_{idx:02d}_{target.name}_form.png"
                form.screenshot(path=str(clip_path))
                print(f"[3/4] Form screenshot saved: {clip_path}")
            else:
                print(f"[3/4] Form selector not found on: {target.url}")

        print("[4/4] 캡처 완료. 브라우저를 닫으려면 Enter를 누르세요.")
        input()
        context.close()


if __name__ == "__main__":
    main()
