# Happy Birthday Muskuuu: project

Files
- `index.html`: the whole website (GitHub Pages serves this file first)
- `og-image.jpg`: 1200x630 link-preview thumbnail (red curtain with the new DP in a gold ring)
- `./birthday-song.mp3`: your song. It starts at 1:46 the moment the counter goes from 18 to 19 and keeps playing until the visitor presses Pause, the song ends, or the project finishes (the last chat message in the final section has been sent). A reload or restart resets everything, including the counter and the 1:46 start.
- `.nojekyll`: tells GitHub Pages to serve the files as they are

Deploy / update on GitHub Pages
1. Upload ALL files to the same repository your site already uses, replacing the old ones. The site address does not change.
2. In `index.html`, Find & Replace `YOUR-USERNAME` with your GitHub username and `YOUR-REPO` with your repository name (4 places in the `<head>`). If your site is at `https://name.github.io/` (no repo name in the address), replace `YOUR-USERNAME.github.io/YOUR-REPO/` with `name.github.io/`.
3. Wait about a minute, then open `https://YOUR-USERNAME.github.io/YOUR-REPO/og-image.jpg` in a browser. If you see the red curtain image, the preview image is public.

Link preview cache
WhatsApp, Facebook, Instagram and others remember the preview of a link for days. For a link that was shared before: Facebook and Instagram, use the Facebook Sharing Debugger (developers.facebook.com/tools/debug) and press "Scrape Again". WhatsApp has no refresh button, so add `?v=2` to the end of the link when you send it (it counts as a new link). A brand-new link shows the new preview straight away.

Countdown
Live countdown to 23 October 2026, 12:00 AM IST (`2026-10-23T00:00:00+05:30`), whatever timezone the visitor is in. The curtain opens only when PREVIEW is clicked.

Check the link preview after publishing
Run `python3 check-link-preview.py https://YOUR-USERNAME.github.io/YOUR-REPO/` (with your real address). It reads your live page the way WhatsApp does and tells you if the title, description and image address are correct.
