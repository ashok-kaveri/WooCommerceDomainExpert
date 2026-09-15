"""Capture the Claude browser pane to a named PNG, for test-document evidence.

The browser tools return screenshots into the conversation but cannot write them
to disk, and the embedded browser refuses localhost connections, so the only
route to a file is a full-screen grab cropped to the pane.

Requires Screen Recording permission for the Claude app. Without it macOS fails
with "could not create image from display".

Calibrate once per session, then capture:

    # 1. inject markers in the page (run via the browser javascript tool):
    #    see --calibrate output for the snippet
    python3 capture_browser.py --calibrate
    python3 capture_browser.py tc01_02_order_page --rect 1532,222,2920,1088

Store the rect and reuse it; re-calibrate if the window or layout moves.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image

DEFAULT_OUT = Path("data/test_documents/screenshots")

MARKER_JS = """
document.querySelectorAll('.__calib').forEach(e => e.remove());
const mk = css => {
  const d = document.createElement('div');
  d.className = '__calib';
  d.style.cssText =
    'position:fixed;z-index:2147483647;width:10px;height:10px;background:#FF00FF;' + css;
  document.body.appendChild(d);
};
mk('top:0;left:0'); mk('top:0;right:0'); mk('bottom:0;left:0'); mk('bottom:0;right:0');
({ innerW: innerWidth, innerH: innerHeight, dpr: devicePixelRatio });
"""


def _screen_grab(dest: Path) -> None:
    result = subprocess.run(
        ["screencapture", "-x", "-t", "png", str(dest)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not dest.exists():
        raise SystemExit(
            "screencapture failed: "
            f"{result.stderr.strip() or 'no output'}\n"
            "Grant Screen Recording to the Claude app in "
            "System Settings -> Privacy & Security, then retry."
        )


def calibrate(tmp: Path) -> tuple[int, int, int, int]:
    """Find the pane rect from magenta corner markers injected into the page."""
    import numpy as np

    raw = tmp / "_calib.png"
    _screen_grab(raw)
    arr = np.array(Image.open(raw).convert("RGB"))
    mask = (arr[:, :, 0] > 200) & (arr[:, :, 1] < 80) & (arr[:, :, 2] > 200)
    ys, xs = np.nonzero(mask)
    raw.unlink(missing_ok=True)
    if not len(xs):
        raise SystemExit(
            "No markers found. Inject them into the page first with the browser "
            "javascript tool:\n\n" + MARKER_JS
        )
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def capture(name: str, rect: tuple[int, int, int, int], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = out_dir / "_raw.png"
    _screen_grab(tmp)
    dest = out_dir / f"{name}.png"
    Image.open(tmp).convert("RGB").crop(rect).save(dest)
    tmp.unlink(missing_ok=True)
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", nargs="?", help="Output filename stem, e.g. tc01_02_order_page")
    parser.add_argument("--rect", help="x0,y0,x1,y1 of the browser pane on screen")
    parser.add_argument("--calibrate", action="store_true", help="Find the pane rect")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    if args.calibrate:
        x0, y0, x1, y1 = calibrate(args.out)
        print(f"rect: {x0},{y0},{x1},{y1}   ({x1 - x0}x{y1 - y0})")
        print("Remove the markers before capturing:")
        print("  document.querySelectorAll('.__calib').forEach(e => e.remove());")
        return 0

    if not args.name or not args.rect:
        parser.error("give a name and --rect, or use --calibrate")

    rect = tuple(int(v) for v in args.rect.split(","))
    if len(rect) != 4:
        parser.error("--rect must be x0,y0,x1,y1")

    path = capture(args.name, rect, args.out)
    width, height = Image.open(path).size
    print(f"{path}  {width}x{height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
