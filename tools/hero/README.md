# Hero video workflow (static/media/hero.mp4)

How the homepage hero montage is produced and verified. The current hero was cut from
the lab's YouTube paper videos; the preferred source going forward is **raw lab footage**
dropped into `tools/hero/raw/` (gitignored — raw files never enter the repo).

## Inputs

1. **Raw clips** in `tools/hero/raw/` — any length, 1080p or better, tripod or gimbal
   shots preferred. No text overlays needed (that's the point: no cropping around slides).
2. **YouTube channel scan** (`yt-dlp` on @ACPLab-wpi) as a supplementary source when a
   paper video has a moment the raw footage doesn't.

## Pipeline

1. **Scan**: build dense contact sheets per candidate video (1 fps minimum — the original
   hero used ~1 frame per 2.5 s, which was too coarse and let the quadrotor drift out of
   frame unnoticed in two clips). Review sheets visually, shortlist segments.
2. **Verify visibility** (the step that prevents the empty-room problem): for every
   shortlisted segment and intended crop, run

   ```bash
   python3 tools/hero/check_visibility.py raw/clip.mp4 --start 13.5 --dur 9 --crop 1920:610:0:290
   ```

   It frame-differences the segment at 6 fps and reports, per sample, whether the moving
   subject sits inside the crop window. **Acceptance: >= 90% of samples OK/PART and no
   OUT/NONE run longer than ~1.5 s.** Trim the segment or move the crop until it passes.
3. **Crop**: only to remove overlay text or to reframe; with clean raw footage prefer the
   full 16:9 frame. All clips are normalized to the same canvas before joining
   (currently 1920x800; with raw footage consider full 1920x1080).
4. **Assemble**: 3-5 clips, 6-9 s each, 24-40 s total. Order bright -> dark -> bright so
   the loop seam (last frame -> first frame) lands bright-to-bright. 0.5 s crossfades via
   ffmpeg `xfade`; each input normalized with `setpts=PTS-STARTPTS,fps=30,settb=AVTB`.
5. **Encode**: `libx264 -crf 25 -pix_fmt yuv420p -movflags +faststart -an`. Keep the file
   under ~8 MB. Muted always (the hero autoplays).
6. **Poster**: grab a frame where a robot is clearly visible:
   `ffmpeg -ss <t> -i hero.mp4 -frames:v 1 -q:v 3 hero-poster.jpg`
7. **Install**: replace `static/media/hero.mp4` and `static/media/hero-poster.jpg`,
   hard-refresh localhost:1313, watch one full loop before pushing.

## Template assembly command

```bash
ffmpeg \
  -ss S0 -t D0 -i clipA.mp4  -ss S1 -t D1 -i clipB.mp4  -ss S2 -t D2 -i clipC.mp4 \
  -filter_complex "\
    [0:v]crop=W:H:X:Y,scale=1920:-2,crop=1920:800,setpts=PTS-STARTPTS,fps=30,settb=AVTB[v0];\
    [1:v]...[v1];[2:v]...[v2];\
    [v0][v1]xfade=transition=fade:duration=0.5:offset=<D0-0.5>[x1];\
    [x1][v2]xfade=transition=fade:duration=0.5:offset=<D0+D1-1.0>[vout]" \
  -map "[vout]" -c:v libx264 -crf 25 -pix_fmt yuv420p -movflags +faststart -an hero.mp4
```

(xfade offsets are cumulative: each one is the running output length so far minus the
fade duration.)
