"""Pull evidence frames out of a video attached to a Trello card.

Used when the user wants the test document built from a recording instead of a
live run. Frames extracted this way are NOT an executed test: label those cases
"Not run (from video)" and describe what the recording shows.

    # what's in it, and where the scene changes are
    python3 video_frames.py run.mov --probe

    # one frame per detected scene change (default)
    python3 video_frames.py run.mov --out data/test_documents/screenshots --prefix tc01

    # or at fixed timestamps
    python3 video_frames.py run.mov --at 0:12 1:05 2:31 --prefix tc02
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"{cmd[0]} failed:\n{result.stderr.strip()[:2000]}")
    return result


def probe(video: Path, threshold: float) -> None:
    meta = json.loads(
        _run(["ffprobe", "-v", "quiet", "-print_format", "json",
              "-show_format", "-show_streams", str(video)]).stdout
    )
    stream = next((s for s in meta["streams"] if s["codec_type"] == "video"), {})
    print(f"duration : {float(meta['format'].get('duration', 0)):.1f}s")
    print(f"size     : {stream.get('width')}x{stream.get('height')}")

    out = _run(["ffmpeg", "-i", str(video), "-filter:v",
                f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"]).stderr
    times = [
        line.split("pts_time:")[1].split()[0]
        for line in out.splitlines() if "pts_time:" in line
    ]
    print(f"scene changes ({len(times)}): {', '.join(times[:40])}")


def extract_scenes(video: Path, out_dir: Path, prefix: str, threshold: float) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    pattern = out_dir / f"{prefix}_scene_%03d.png"
    _run(["ffmpeg", "-y", "-i", str(video), "-vf",
          f"select='gt(scene,{threshold})'", "-vsync", "vfr", str(pattern)])
    return sorted(out_dir.glob(f"{prefix}_scene_*.png"))


def extract_at(video: Path, stamps: list[str], out_dir: Path, prefix: str) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for idx, stamp in enumerate(stamps, start=1):
        dest = out_dir / f"{prefix}_{idx:02d}.png"
        _run(["ffmpeg", "-y", "-ss", stamp, "-i", str(video),
              "-frames:v", "1", str(dest)])
        made.append(dest)
    return made


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", type=Path, default=Path("data/test_documents/screenshots"))
    parser.add_argument("--prefix", default="video")
    parser.add_argument("--at", nargs="+", metavar="TS", help="Timestamps, e.g. 0:12 1:05")
    parser.add_argument("--threshold", type=float, default=0.3,
                        help="Scene-change sensitivity, 0-1 (default 0.3)")
    parser.add_argument("--probe", action="store_true", help="Report duration and scene cuts only")
    args = parser.parse_args()

    if not args.video.exists():
        raise SystemExit(f"no such video: {args.video}")

    if args.probe:
        probe(args.video, args.threshold)
        return 0

    frames = (extract_at(args.video, args.at, args.out, args.prefix) if args.at
              else extract_scenes(args.video, args.out, args.prefix, args.threshold))

    for frame in frames:
        print(frame)
    print(f"\n{len(frames)} frame(s). Review each one and keep only those that "
          f"evidence a specific test case; delete the rest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
