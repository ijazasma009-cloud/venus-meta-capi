# Creative assets

Copied from `Desktop\Venus-Aesthetics\03-creative-assets` and
`04-ads-and-campaigns` on 24 September 2026.

**139 files, 201 MB.** The source folders hold 164 files and 872 MB, so some
things were left behind. Everything left behind is listed below with its exact
path, so nothing is lost, it is just not in git.

---

## Why not all of it

Three reasons, in order of how hard they are:

**1. GitHub hard-rejects any file over 100 MB.** Three files breach it:

| Size | File |
|---|---|
| 169.0 MB | `03-creative-assets/doctor-videos/Kabeer_Laser.mp4` |
| 164.1 MB | `03-creative-assets/doctor-videos/Dr. Raheela Danish.mp4` |
| 140.0 MB | `04-ads-and-campaigns/k-glow-launch/Venus-K-Glow-Complete-Final-Package.zip` |

A push containing any of these fails. Not a preference, a hard block.

**2. A Claude session cannot watch video.** The 8 MP4 files are 501 MB of the
872 MB. A session can read images, PDFs and documents, but an MP4 is opaque
weight that every future clone has to download. The `.psd` is the same, nothing
can open it.

**3. The zip is redundant.** `Venus-K-Glow-Complete-Final-Package.zip` is the
packaged copy of files that are already present unpacked in
`k-glow-launch/Venus-K-Glow-Complete-Final-Package-v4/`.

---

## What is here

| Type | Files | Size |
|---|---|---|
| Images, png / jpg / jpeg | 119 | 144 MB |
| Documents, pdf / docx / xlsx | 15 | 52 MB |
| html / js / py / json | 13 | ~4 MB |
| Fonts, ttf | 3 | small |

Folder structure mirrors the Desktop layout exactly, so a path in a brief still
resolves.

The bulk is the **K-Glow launch package**, which has two full creative routes
(`Version-1-Korean-First` and the v4 package) with box, mailer, flyer and social
artwork, plus the team plan as both docx and pdf.

---

## What is NOT here, and where to find it

All paths below are relative to `Desktop\Venus-Aesthetics\`.

### Video, 8 files, 501 MB

| Size | Path |
|---|---|
| 169.0 MB | `03-creative-assets/doctor-videos/Kabeer_Laser.mp4` |
| 164.1 MB | `03-creative-assets/doctor-videos/Dr. Raheela Danish.mp4` |
| 74.5 MB | `03-creative-assets/doctor-videos/Video Project 37.mp4` |
| 36.7 MB | `04-ads-and-campaigns/google-reviews-milestone/Venus_10000_Voices_FINAL_1080x1920.mp4` |
| 29.3 MB | `04-ads-and-campaigns/google-reviews-milestone/00-superseded-v1/Venus_10000_Voices_Master_1080x1920.mp4` |
| 15.5 MB | `04-ads-and-campaigns/google-reviews-milestone/Venus_10000_Voices_FINAL_share.mp4` |
| rest | same folders |

### Other excluded

| Path | Why |
|---|---|
| `04-ads-and-campaigns/k-glow-launch/Venus-K-Glow-Complete-Final-Package.zip` | 140 MB, over the limit, and redundant |
| `03-creative-assets/Azadi sale.psd` | 19.4 MB, nothing can open it |
| `04-ads-and-campaigns/google-reviews-milestone/01-verification/reviews-used.csv` | Real reviewer names |
| `04-ads-and-campaigns/google-reviews-milestone/01-verification/verified-counts.csv` | Same folder, same reason |
| `04-ads-and-campaigns/google-reviews-milestone/01-verification/raw-google-capture.json` | Raw Google capture, reviewer names |

The reviews files were held back under the standing rule about real personal
data. They are public Google reviews rather than patient records, so if they
are wanted here, say so and they go in.

### The separate video library

The 201 clips on Google Drive are a different set again, indexed in
`../content-calendar/research/drive_inventory.json` with a Drive file `id` on
every entry, and runtimes for 66 of them in `durations_clean.json`.

---

## If you want the videos in the repo anyway

Git LFS is installed on the machine, version 3.7.1, and it would take files over
100 MB. Before doing it, the cost:

- GitHub free tier gives **1 GB LFS storage and 1 GB bandwidth per month**.
- The videos are 501 MB, the zip another 140 MB. That is **most of the free
  storage gone at once**.
- Bandwidth is charged **per clone**. One cloud session cloning this repo would
  use roughly 640 MB of the 1 GB monthly allowance. **The second clone in the
  same month would fail.**
- More storage and bandwidth is a paid data pack.

Given a session cannot watch the video anyway, the recommendation is to leave
them on Drive and on the Desktop. But it is a one-command change if wanted.

---

## Note on names

Two video filenames name individuals, and some artwork names talent. The video
files are not in this repo. The images that are here are finished marketing
creative, made to be published.
