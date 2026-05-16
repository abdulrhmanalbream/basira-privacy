# Basira — Privacy Policy site

Public-facing privacy policy for the **Basira | Digital Balance** Android application.

Hosted via GitHub Pages.

## Files
- `index.html` — language selector landing page
- `ar.html` — Arabic privacy policy
- `en.html` — English privacy policy
- `.nojekyll` — disables Jekyll processing (we ship pure HTML)
- `build.py` — regenerates `ar.html` and `en.html` from the project's source markdown files (`PRIVACY_POLICY_AR.md`, `PRIVACY_POLICY_EN.md`)

## Updating the policy

1. Edit `PRIVACY_POLICY_AR.md` and/or `PRIVACY_POLICY_EN.md` in the source repo.
2. Run `python build.py` to regenerate the HTML.
3. Copy the resulting `ar.html` / `en.html` to this Pages repo.
4. Commit and push.

## Contact

abdulrhman.qt@gmail.com
