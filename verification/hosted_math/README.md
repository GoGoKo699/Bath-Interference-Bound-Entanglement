# Check mathematics on GitHub

This read-only collector compares the mathematics displayed by GitHub with the
Markdown source at one exact commit. It checks every expression at desktop and
narrow viewport widths, including formulas in tables, and saves HTML, screenshots,
MathML, source hashes and a machine-readable report. Review the screenshots as
well: automated structure and geometry checks do not establish scientific
correctness or complete visual legibility.

The collector needs Node.js 18 or later, Python 3.10 or later, Git, Playwright and
MathJax. Install the browser dependencies outside this checkout. For example,
with an existing temporary directory assigned to `RENDER_DEPS`:

```bash
npm install --prefix "$RENDER_DEPS" playwright@1.56.1 mathjax-full@3.2.1
node "$RENDER_DEPS/node_modules/playwright/cli.js" install chromium
NODE_PATH="$RENDER_DEPS/node_modules" node verification/hosted_math/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Bath-Interference-Bound-Entanglement \
  --revision "$(git rev-parse HEAD)" \
  --contract verification/hosted_math/math-contract.json \
  --output /absolute/new-empty-capture-directory
```

Replace the example output directory with an empty directory outside the
checkout. The default scope is every tracked Markdown page at the supplied
commit; repeated `--page PATH` options select an intentional smaller sample.
The checked commit must already be available on public GitHub. The browser uses
a fresh anonymous context and does not authenticate or edit repository content.

`capture_hosted_math.cjs` invokes `check_rendered_math.py`, which also supports
standalone `inventory` and `check` commands. A successful capture compares all
source expressions with actual hosted MathML at widths 1440 and 760 pixels.
The report records the exact commit, tree, page scope, source hashes, comparison
results and artifact hashes. It does not certify other browser versions or
future changes to GitHub's renderer.

The text contract supplies explicit operand and inequality checks for headline
results and the duration table. Each entry is bound to the hash of its source
expression. When editing one of those formulas, review its meaning and update
the corresponding contract before running the full capture.

The corresponding GitHub Actions job has `contents: read`, does not persist
checkout credentials, and uploads diagnostic artifacts for seven days. Those
expiring artifacts are working evidence, not a permanent archival record.
See [the numerical verification guide](../README.md) for the separate checks of
the generator and entanglement formulas.
