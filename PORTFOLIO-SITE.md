# INNNX. responsive portfolio

Static GitHub Pages website: `docs/`. The profile README, original SVG files and all `portfolio/*.md` documents are preserved.

## Structure

- `docs/{zh,en,es}/index.html`: localized homepage.
- Four category pages in each language.
- Four documented project pages in each language.
- `docs/assets`: shared CSS, JavaScript and city illustration extracted from the existing profile SVG.
- `tools/build_site.py`: dependency-free generator and complete trilingual content.
- `tools/verify_site.cjs`: browser checks (requires Playwright and Microsoft Edge).
- `.github/workflows/pages.yml`: deploys only `docs/` using GitHub Pages Actions.

## Updating

Edit the translations together in `tools/build_site.py`, then run `python tools/build_site.py`. The generator leaves CSS, JavaScript, the profile and existing documentation untouched. Serve `docs/` at port 8765 and run `node tools/verify_site.cjs` with Playwright available. No runtime dependencies, analytics, external fonts, cookies or build step are required for visitors. Theme and language preferences are stored in the visitor's browser; failure or unavailability of storage does not block navigation.

## Source review — 2026-10-13

The four original category documents and current public project READMEs were reviewed. Project details link to the public repositories and existing authentic screenshots. No private implementation, prompts, signing files or backup archives are included.

- Linux Server Hardening: completed within the documented lab scope. Automatic failed-login detection was not directly tested; a fully updated server was not established.
- Party Games: the current root README and public v1.0.0 pre-release supersede the older category/documentation claim that no playable package is public. The website links to the actual Android demo release and checksums; it does not claim a Google Play release or validated iOS build.
- BlockSlayer: prototype, no public installer. Retains upstream attribution and limitations; the existing home is English and says BLOCK CRUSH.
- ESP32: reviewed public commit `d29f586` and preceding firmware/media commits. The existing V1 URL now presents PaperRobot V2 integrated firmware, 11 recorded compilation passes and an owner-provided real build demo. Six face designs, IR-driven face/yaw, touch nod, wiring and limits were checked against public source. V1/history remains linked through the repository. V2 retains Made by Z inspiration and is not claimed as independent; V3 is planned. Per-test physical results, flashed firmware hash, assembly photos and dimensions remain pending. Permanent reference: https://xhslink.cn/m/5y0F9KIVkvd.
- Featured: no selected projects, matching the original document.

All core pages and navigation have equivalent Chinese, English and Spanish content. Linked external documents retain their original available languages. Public screenshots are served from their original public repositories; Party Games uses corresponding language images, while BlockSlayer's real English interface is identified in every language.

GitHub Pages should use **GitHub Actions** as its publishing source. Only the website directory is uploaded; repository reference documents and tools are not part of the deployed artifact.

## Website validation and publication review

- 108 page/viewport checks at 360, 390, 768 and 1440 pixels: no overflow, working local links, equivalent language navigation, theme persistence and keyboard skip navigation.
- 54 WCAG A/AA automated audits across all 27 translated pages in both themes, with no detected violations other than the original video's missing captions. This media limitation is disclosed; a direct playback/download link is provided. Automated checks do not certify all accessibility requirements.
- Canonical URLs, localized descriptions, three language alternates plus x-default, Open Graph/Twitter preview, 28 sitemap URLs and a styled trilingual 404 recovery page.
- No external fonts or libraries on visitor pages. Video uses `preload="none"`, local preview and no autoplay. Public screenshots load lazily. Shared social preview is rendered from the preserved INNNX city illustration and identity.
- Reviewed the public media preview for visible personal information; it shows the cardboard robot on a desk. The existing public video provenance records removal of location/device metadata. No local original MOV, private backups, account data or private application source is included.
- Scanned deployable HTML/assets and generator for common secret patterns, private key markers, local user paths and private LAN addresses; no matches. README, profile artwork and original category documents are unchanged.
- Metadata/accessibility check: run `node tools/verify_metadata.cjs` with Playwright and `axe-core` installed, or set `AXE_SCRIPT` to an existing axe-core browser script. Serve `docs/` on port 8765 first.

`robots.txt` is shipped under the project site path. Crawlers normally consult host-root `/robots.txt`; this repository cannot control that file on the shared github.io host. All published pages remain crawlable, and the sitemap has absolute canonical URLs.
