#!/usr/bin/env python3
"""Check that the moving subject (the robot) stays inside a crop window for a video segment.

Used when cutting hero.mp4 clips: coarse contact sheets can miss the moments where the
quadrotor leaves the frame or the crop band, so this samples densely (default 6 fps),
finds motion by frame differencing, and reports per-sample whether the motion sits
inside the intended crop rectangle.

Usage:
  python3 check_visibility.py VIDEO --start 13.5 --dur 9 --crop 1920:610:0:290 [--fps 6]

crop format matches ffmpeg: W:H:X:Y in source pixels.
Verdict per sample: OK (motion inside crop), PART (split), OUT (motion outside crop),
NONE (no motion found - subject likely gone or hovering perfectly still).

Stdlib only; needs ffmpeg on PATH, or set FFMPEG=/path/to/ffmpeg, or have imageio_ffmpeg installed.
"""
import argparse, os, shutil, subprocess, sys

AW, AH = 192, 108  # analysis resolution (16:9); crops are mapped into this space


def find_ffmpeg():
    if os.environ.get("FFMPEG"):
        return os.environ["FFMPEG"]
    if shutil.which("ffmpeg"):
        return "ffmpeg"
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg not found: install it, set FFMPEG=, or pip install imageio-ffmpeg")


def probe_size(ff, video):
    out = subprocess.run([ff, "-i", video], capture_output=True, text=True).stderr
    import re
    m = re.search(r"Video:.* (\d{2,5})x(\d{2,5})", out)
    if not m:
        sys.exit("could not determine video resolution")
    return int(m.group(1)), int(m.group(2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--dur", type=float, required=True)
    ap.add_argument("--crop", default=None, help="W:H:X:Y in source pixels (default: full frame)")
    ap.add_argument("--fps", type=float, default=6.0)
    ap.add_argument("--diff-threshold", type=int, default=25, help="pixel delta that counts as motion")
    ap.add_argument("--min-motion", type=int, default=6, help="motion pixels below this = NONE")
    args = ap.parse_args()

    ff = find_ffmpeg()
    sw, sh = probe_size(ff, args.video)
    if args.crop:
        cw, ch, cx, cy = (int(v) for v in args.crop.split(":"))
    else:
        cw, ch, cx, cy = sw, sh, 0, 0
    # crop rect in analysis space
    rx0, ry0 = cx * AW / sw, cy * AH / sh
    rx1, ry1 = (cx + cw) * AW / sw, (cy + ch) * AH / sh

    cmd = [ff, "-loglevel", "error", "-ss", str(args.start), "-t", str(args.dur),
           "-i", args.video, "-vf", f"fps={args.fps},scale={AW}:{AH},format=gray",
           "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (AW * AH)
    frames = [raw[i * AW * AH:(i + 1) * AW * AH] for i in range(n)]
    if n < 2:
        sys.exit("segment too short / decode failed")

    print(f"{args.video}  start={args.start}s dur={args.dur}s  crop={cw}:{ch}:{cx}:{cy}  "
          f"({n} samples @ {args.fps}/s)")
    print(f"{'t(s)':>7} {'motionpx':>9} {'in-crop%':>9}  verdict")
    bad = 0
    for i in range(1, n):
        a, b = frames[i - 1], frames[i]
        total = inside = 0
        sx = sy = 0.0
        for p in range(AW * AH):
            if abs(a[p] - b[p]) > args.diff_threshold:
                total += 1
                x, y = p % AW, p // AW
                sx += x; sy += y
                if rx0 <= x <= rx1 and ry0 <= y <= ry1:
                    inside += 1
        t = args.start + i / args.fps
        if total < args.min_motion:
            verdict = "NONE"
        else:
            frac = inside / total
            verdict = "OK" if frac >= 0.8 else ("PART" if frac >= 0.4 else "OUT")
        if verdict in ("OUT", "NONE"):
            bad += 1
        pct = f"{100*inside/total:7.0f}%" if total else "      -"
        print(f"{t:7.2f} {total:9d} {pct:>9}  {verdict}")
    frac_bad = bad / (n - 1)
    print(f"\nsummary: {n-1-bad}/{n-1} samples OK/PART ({100*(1-frac_bad):.0f}%). "
          f"Target: >=90% and no run of OUT/NONE longer than ~1.5s.")
    sys.exit(0 if frac_bad <= 0.10 else 2)


if __name__ == "__main__":
    main()
