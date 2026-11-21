# Open flags

Conflicts and open questions with no proposed change yet (CLAUDE.md section 13). Include open items in the next change email; close them here with a date.

## Open
- 2026-11-21 · **Privacy page is out of date (Jack: compliance, section 15).** `/privacy/` still says "The form is a Netlify Form once this folder is deployed. Until then it is only a local page and does not submit anywhere" and "It does not name one today, because none has been bought." The site is live on chencharuyishun.sg and the form submits to Netlify Forms. Proposed text: "Enquiries sent through the form are stored by Netlify Forms for this site, chencharuyishun.sg, and read by Jack Leow of PropNex Realty Pte Ltd." Not changed: needs Jack's approval.
- 2026-11-21 · **Project name not confirmed.** "Chencharu Central Residences" is the PropNex ebook's marketing name. Run the rename protocol (section 3C) as soon as the developer, HDB or 2 reputable sources confirm a name.
- 2026-11-21 · **Homes: 875 vs about 860.** HDB's estimate and the ebook say 875; Evia told The Business Times about 860 (Sep 2025). Both stay Reported until the developer publishes one number.
- 2026-11-21 · **Preview / booking dates** (16 and 30 Jan 2027) appear on one agent page as TBC and conflict with other write-ups. No `Event` schema until Confirmed.
- 2026-11-21 · **Walk to Khatib MRT**: sources conflict (within 450 m per Gamuda; under 6 minutes per the ebook; 330-350 m and 460 m on other pages). Needs Jack's timed walk.
- 2026-11-21 · **Developer's sales licence.** One agent page (dated 10 Oct 2026) says a developer's licence was issued on 30 Sep 2026. Not a source (section 5). Check URA's developer licence records before stating it; no change made.

## Closed
- 2026-11-21 · **Netlify does not auto-deploy pushes (Jack).** Pushes of 0ac6bc7 and 65bb882 to `main` started no Netlify build; both were deployed by triggering a build through the Netlify API (site 3754e3c3-bf73-4239-b354-7438342c40d0). The site's build settings point at Jackleow153/chencharu-central-residence, branch main, builds not stopped, so the GitHub webhook / Netlify GitHub app link is the likely cause. Fix: Netlify > Site configuration > Build & deploy > Continuous deployment > Link repository again. Until fixed, every push must be followed by a manual deploy, and the daily run's "fetch the live page until it shows the change" step will fail.
  - Closed 2026-11-21: the GitHub repo had no webhook to Netlify (One Chuan Grove's repo has one). Jack added https://api.netlify.com/hooks/github (JSON; push, pull request, delete); ping answered 204. This push is the auto-deploy test.
