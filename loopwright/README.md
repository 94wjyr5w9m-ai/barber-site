# Loopwright: landing page and waitlist

`index.html` is a self-contained landing page with a working waitlist form. It needs no build step.

## Deploy (Netlify, recommended)

1. Create a site on Netlify from this repo with **base/publish directory** `loopwright`. You can also drag the `loopwright` folder onto app.netlify.com/drop.
2. In **Site configuration → Forms**, turn on **form detection**, then redeploy.
3. Signups show up under **Forms → waitlist**. You can turn on email notifications there, or export to CSV.

## Deploy anywhere else (GitHub Pages, Vercel, etc.)

1. Create a free form at https://formspree.io.
2. In `index.html`, set `FORM_ENDPOINT` to its URL, for example `"https://formspree.io/f/abcdwxyz"`.

## Before launch

- Check that the name is available as a domain and on social handles (for example loopwright.ai or getloopwright.com), and run a trademark search.
- The run log in the hero and the "Typical" savings figures are illustrative. Replace them with real numbers once you have pilot results.
