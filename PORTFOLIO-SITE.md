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

## Source review — 2026-10-10

The four original category documents and current public project READMEs were reviewed. Project details link to the public repositories and existing authentic screenshots. No private implementation, prompts, signing files or backup archives are included.

- Linux Server Hardening: completed within the documented lab scope. Automatic failed-login detection was not directly tested; a fully updated server was not established.
- Party Games: the current root README and public v1.0.0 pre-release supersede the older category/documentation claim that no playable package is public. The website links to the actual Android demo release and checksums; it does not claim a Google Play release or validated iOS build.
- BlockSlayer: prototype, no public installer. Retains upstream attribution and limitations; the existing home is English and says BLOCK CRUSH.
- ESP32 V1: inspired prototype with static OLED code, hardware validation unconfirmed. Permanent inspiration link: https://xhslink.cn/m/5y0F9KIVkvd. V2/V3 are plans for independent development only.
- Featured: no selected projects, matching the original document.

All core pages and navigation have equivalent Chinese, English and Spanish content. Linked external documents retain their original available languages. Public screenshots are served from their original public repositories; Party Games uses corresponding language images, while BlockSlayer's real English interface is identified in every language.

GitHub Pages should use **GitHub Actions** as its publishing source. Only the website directory is uploaded; repository reference documents and tools are not part of the deployed artifact.
