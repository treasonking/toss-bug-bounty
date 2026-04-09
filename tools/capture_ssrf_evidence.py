#!/usr/bin/env python3
"""Capture SSRF evidence with minimal manual effort.

What this script does:
1) Opens Chromium (visible).
2) You log in manually.
3) You reproduce the SSRF-related action once in the app.
4) Script saves:
   - screenshots (before/after)
   - matching request/response raw files
   - summary markdown

No app source-code analysis is required.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
from typing import List

from playwright.sync_api import BrowserContext, Request, Response, sync_playwright


# Edit these if needed.
TARGET_HOST_HINTS = [
    "bugbounty.toss.sb",
    "/link/preview",
    "/preview",
    "/webhook",
]


def now_stamp() -> str:
    return datetime.now().strftime("%H%M%S")


def sanitize_name(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "_", value)
    return value[:80].strip("_") or "artifact"


def save_request(req: Request, out_path: Path) -> None:
    headers = "\n".join(f"{k}: {v}" for k, v in req.headers.items())
    body = req.post_data or ""
    text = (
        f"{req.method} {req.url}\n"
        f"{headers}\n\n"
        f"{body}\n"
    )
    out_path.write_text(text, encoding="utf-8")


def save_response(resp: Response, out_path: Path) -> None:
    req = resp.request
    try:
        body = resp.text()
    except Exception:
        body = "<non-text response body>"
    headers = "\n".join(f"{k}: {v}" for k, v in resp.headers.items())
    text = (
        f"{req.method} {req.url}\n"
        f"Status: {resp.status}\n"
        f"{headers}\n\n"
        f"{body}\n"
    )
    out_path.write_text(text, encoding="utf-8")


def is_interesting(url: str) -> bool:
    u = url.lower()
    return any(hint.lower() in u for hint in TARGET_HOST_HINTS)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    date_dir = root / "evidence" / datetime.now().strftime("%Y-%m-%d") / "url_input"
    reqres_dir = date_dir / "reqres"
    screens_dir = date_dir / "screens"
    notes_dir = date_dir / "notes"
    reqres_dir.mkdir(parents=True, exist_ok=True)
    screens_dir.mkdir(parents=True, exist_ok=True)
    notes_dir.mkdir(parents=True, exist_ok=True)

    user_data_dir = root / ".playwright-profile"
    user_data_dir.mkdir(parents=True, exist_ok=True)

    captured: List[str] = []

    with sync_playwright() as p:
        context: BrowserContext = p.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            headless=False,
            viewport={"width": 1600, "height": 1200},
        )
        page = context.new_page()
        page.goto("https://bugbounty.toss.im/", wait_until="domcontentloaded")

        def on_request(req: Request) -> None:
            if not is_interesting(req.url):
                return
            stamp = now_stamp()
            base = sanitize_name(req.url.split("?")[0].split("/")[-1] or "request")
            out = reqres_dir / f"{stamp}_ssrf_req_{base}.txt"
            save_request(req, out)
            captured.append(str(out.relative_to(root)))
            print(f"[capture] request -> {out}")

        def on_response(resp: Response) -> None:
            if not is_interesting(resp.url):
                return
            stamp = now_stamp()
            base = sanitize_name(resp.url.split("?")[0].split("/")[-1] or "response")
            out = reqres_dir / f"{stamp}_ssrf_resp_{base}.txt"
            save_response(resp, out)
            captured.append(str(out.relative_to(root)))
            print(f"[capture] response -> {out}")

        context.on("request", on_request)
        context.on("response", on_response)

        print("[1/4] 브라우저가 열렸습니다. 로그인 후 SSRF 재현 동작을 1회 수행하세요.")
        print("[2/4] 재현 직전 Enter를 누르면 before 캡처를 찍습니다.")
        input()
        before = screens_dir / f"{now_stamp()}_ssrf_before.png"
        page.screenshot(path=str(before), full_page=True)
        captured.append(str(before.relative_to(root)))
        print(f"[capture] screenshot -> {before}")

        print("[3/4] 이제 앱에서 SSRF 관련 동작(예: url=http://bugbounty.toss.sb)을 수행하세요.")
        input("동작이 끝나면 Enter를 누르세요...")
        after = screens_dir / f"{now_stamp()}_ssrf_after.png"
        page.screenshot(path=str(after), full_page=True)
        captured.append(str(after.relative_to(root)))
        print(f"[capture] screenshot -> {after}")

        summary = notes_dir / f"{now_stamp()}_ssrf_capture_summary.md"
        summary.write_text(
            "# SSRF Capture Summary\n\n"
            "아래 파일들이 자동 수집되었습니다.\n\n"
            + "\n".join(f"- `{p}`" for p in captured),
            encoding="utf-8",
        )
        print(f"[capture] summary -> {summary}")
        print("[4/4] 완료. Enter를 누르면 브라우저를 닫습니다.")
        input()
        context.close()


if __name__ == "__main__":
    main()
