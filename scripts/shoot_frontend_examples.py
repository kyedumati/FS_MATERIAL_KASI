#!/usr/bin/env python3
"""Render every example page in FRONTEND/HTML_CSS/examples/ to PNG screenshots.

Each example is a real file. The screenshot is what Chrome actually draws, driven
through the DevTools protocol so we can emulate a phone width and scroll the page.

Usage:
    python3 scripts/shoot_frontend_examples.py            # all lessons
    python3 scripts/shoot_frontend_examples.py lesson05   # one lesson folder

Output: FRONTEND/HTML_CSS/screens/<lesson>_<file><suffix>.png
Needs: Google Chrome, Pillow, websockets (pip install websockets).
"""

from __future__ import annotations

import asyncio
import base64
import json
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

import websockets
from PIL import Image, ImageChops, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "FRONTEND" / "HTML_CSS" / "examples"
SCREENS = ROOT / "FRONTEND" / "HTML_CSS" / "screens"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
PORT = 9333
PADDING = 16

DEFAULT = [{"width": 880}]

# Per-example shots. Keys: width, height (viewport; default 800), mobile (phone
# emulation; default width < 600), scroll (pixels), full (whole page; default
# True unless scroll is set), suffix (added to the file name), edge (capture the
# full page width and draw a dashed red line where the screen ends), tab (press
# the Tab key this many times), hover (move the mouse over this CSS selector).
SHOTS: dict[str, list[dict]] = {
    "lesson09/02_button_states.html": [
        {"width": 880, "suffix": "_default"},
        {"width": 880, "suffix": "_hover", "hover": "#apply"},
        {"width": 880, "suffix": "_focus", "tab": 1},
    ],
    "lesson09/04_skip_link.html": [
        {"width": 880, "suffix": "_default"},
        {"width": 880, "suffix": "_tab", "tab": 1},
    ],
    "lesson05/08_sticky.html": [
        {"width": 880, "height": 360, "suffix": "_top", "full": False},
        {"width": 880, "height": 360, "scroll": 520, "suffix": "_scrolled"},
    ],
    "lesson05/03_auto_fit.html": [
        {"width": 880, "suffix": "_880"},
        {"width": 420, "suffix": "_420"},
    ],
    "lesson07/08_scroll_wrapper.html": [{"width": 375, "suffix": "_375", "edge": True}],
    "lesson07/07_wide_table.html": [{"width": 375, "suffix": "_375", "edge": True}],
    "lesson08/01_no_viewport.html": [{"width": 375, "suffix": "_375", "full": False, "height": 560}],
    "lesson08/02_with_viewport.html": [{"width": 375, "suffix": "_375", "full": False, "height": 560}],
    "lesson08/03_fixed_width.html": [{"width": 375, "suffix": "_375", "edge": True}],
    "lesson08/04_mobile_first.html": [
        {"width": 375, "suffix": "_375"},
        {"width": 880, "suffix": "_880"},
    ],
    "lesson08/05_nav.html": [
        {"width": 375, "suffix": "_375"},
        {"width": 880, "suffix": "_880"},
    ],
    "lesson08/06_directory.html": [
        {"width": 375, "suffix": "_375"},
        {"width": 880, "suffix": "_880"},
    ],
    "lesson08/07_clamp.html": [
        {"width": 375, "suffix": "_375"},
        {"width": 880, "suffix": "_880"},
    ],
    "lesson08/08_dashboard.html": [
        {"width": 375, "suffix": "_375"},
        {"width": 880, "suffix": "_880"},
    ],
    "lesson08/09_picture.html": [
        {"width": 375, "suffix": "_375"},
        {"width": 880, "suffix": "_880"},
    ],
}


# Pages outside examples/ that lessons show: (path from FRONTEND/HTML_CSS, output name, shot).
EXTRA: list[tuple[str, str, dict]] = [
    ("labs/L09_final_project/solution/index.html", "lesson09_portal_home", {"width": 880, "suffix": "_880"}),
    ("labs/L09_final_project/solution/index.html", "lesson09_portal_home", {"width": 375, "suffix": "_375"}),
    ("labs/L09_final_project/solution/apply-leave.html", "lesson09_portal_leave", {"width": 880, "suffix": "_880"}),
]


def trim_bottom(png: Path) -> None:
    """Crop empty rows below the content, keeping a little padding."""
    img = Image.open(png).convert("RGB")
    background = img.getpixel((img.width - 1, img.height - 1))
    diff = ImageChops.difference(img, Image.new("RGB", img.size, background))
    box = diff.getbbox()
    if box is None:
        return
    bottom = min(img.height, box[3] + PADDING)
    img.crop((0, 0, img.width, bottom)).save(png, optimize=True)


class Page:
    def __init__(self, ws):
        self.ws = ws
        self.next_id = 0

    async def send(self, method: str, params: dict | None = None) -> dict:
        self.next_id += 1
        msg_id = self.next_id
        await self.ws.send(json.dumps({"id": msg_id, "method": method, "params": params or {}}))
        while True:
            msg = json.loads(await self.ws.recv())
            if msg.get("id") == msg_id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    async def wait_event(self, name: str, timeout: float = 15) -> None:
        end = time.monotonic() + timeout
        while time.monotonic() < end:
            msg = json.loads(await asyncio.wait_for(self.ws.recv(), timeout))
            if msg.get("method") == name:
                return
        raise TimeoutError(name)


async def shoot(page: Page, file: Path, shot: dict) -> Path:
    width = shot["width"]
    height = shot.get("height", 800)
    mobile = shot.get("mobile", width < 600)
    scroll = shot.get("scroll", 0)
    full = shot.get("full", not scroll)
    base = shot.get("name", f"{file.parent.name}_{file.stem}")
    out = SCREENS / f"{base}{shot.get('suffix', '')}.png"

    await page.send("Emulation.setDeviceMetricsOverride", {
        "width": width, "height": height, "deviceScaleFactor": 1, "mobile": mobile,
    })
    await page.send("Page.navigate", {"url": file.as_uri()})
    await page.wait_event("Page.loadEventFired")
    await asyncio.sleep(0.3)
    if scroll:
        await page.send("Runtime.evaluate", {"expression": f"window.scrollTo(0, {scroll})"})
        await asyncio.sleep(0.2)
    for _ in range(shot.get("tab", 0)):
        for kind in ("rawKeyDown", "keyUp"):
            await page.send("Input.dispatchKeyEvent", {
                "type": kind, "key": "Tab", "code": "Tab", "windowsVirtualKeyCode": 9})
        await asyncio.sleep(0.1)
    if "hover" in shot:
        box = await page.send("Runtime.evaluate", {
            "expression": f"(() => {{ const r = document.querySelector({json.dumps(shot['hover'])})"
                          f".getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; }})()",
            "returnByValue": True})
        x, y = box["result"]["value"]
        await page.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})
        await asyncio.sleep(0.4)

    params: dict = {"format": "png"}
    if full:
        metrics = await page.send("Page.getLayoutMetrics")
        content = metrics["cssContentSize"]
        capture_width = width
        if shot.get("edge"):
            sw = await page.send("Runtime.evaluate", {
                "expression": "document.documentElement.scrollWidth", "returnByValue": True})
            capture_width = max(width, sw["result"]["value"])
        params["captureBeyondViewport"] = True
        params["clip"] = {"x": 0, "y": 0, "width": capture_width,
                          "height": max(content["height"], 1), "scale": 1}
    data = await page.send("Page.captureScreenshot", params)
    out.write_bytes(base64.b64decode(data["data"]))
    if full:
        trim_bottom(out)
    if shot.get("edge"):
        draw_edge(out, width)
    return out


def draw_edge(png: Path, x: int) -> None:
    """Draw a dashed red line where the screen ends, plus a grey area beyond it."""
    img = Image.open(png).convert("RGB")
    canvas = Image.new("RGB", (max(img.width, x + 40), img.height), "#e5e7eb")
    canvas.paste(img, (0, 0))
    draw = ImageDraw.Draw(canvas)
    for y in range(0, canvas.height, 12):
        draw.line([(x, y), (x, y + 6)], fill="#dc2626", width=3)
    canvas.save(png, optimize=True)


async def run(files: list[Path], include_extra: bool) -> int:
    profile = tempfile.mkdtemp(prefix="shoot-chrome-")
    chrome = subprocess.Popen(
        [str(CHROME), "--headless=new", "--disable-gpu", "--hide-scrollbars",
         f"--remote-debugging-port={PORT}", f"--user-data-dir={profile}", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        targets = None
        for _ in range(50):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/list") as r:
                    targets = [t for t in json.load(r) if t["type"] == "page"]
                if targets:
                    break
            except OSError:
                pass
            time.sleep(0.2)
        if not targets:
            print("Could not connect to Chrome", file=sys.stderr)
            return 1
        async with websockets.connect(targets[0]["webSocketDebuggerUrl"], max_size=None) as ws:
            page = Page(ws)
            await page.send("Page.enable")
            count = 0
            for file in files:
                key = f"{file.parent.name}/{file.name}"
                for shot in SHOTS.get(key, DEFAULT):
                    out = await shoot(page, file, shot)
                    print(f"  {out.relative_to(ROOT)}")
                    count += 1
            if include_extra:
                for rel, name, shot in EXTRA:
                    out = await shoot(page, ROOT / "FRONTEND" / "HTML_CSS" / rel, {**shot, "name": name})
                    print(f"  {out.relative_to(ROOT)}")
                    count += 1
            print(f"{count} screenshot(s)")
        return 0
    finally:
        chrome.kill()
        chrome.wait()
        shutil.rmtree(profile, ignore_errors=True)


def main() -> int:
    if not CHROME.exists():
        print(f"Chrome not found at {CHROME}", file=sys.stderr)
        return 1
    SCREENS.mkdir(parents=True, exist_ok=True)
    folders = [EXAMPLES / a for a in sys.argv[1:]] or sorted(p for p in EXAMPLES.iterdir() if p.is_dir())
    files = [f for folder in folders for f in sorted(folder.glob("*.html"))]
    include_extra = not sys.argv[1:] or "lesson09" in sys.argv[1:]
    return asyncio.run(run(files, include_extra))


if __name__ == "__main__":
    raise SystemExit(main())
