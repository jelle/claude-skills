# Claude Skills

A personal collection of [Claude Code](https://docs.claude.com/claude-code) skills I use day-to-day. Some are general-purpose, some are wired to my own workflow — share what's useful, ignore the rest.

If you're new to skills: a skill is just a folder with a `SKILL.md` file that Claude Code auto-loads. The frontmatter `description` decides when it triggers. Drop the folder into `~/.claude/skills/` and Claude picks it up.

## What's in here

### Research & thinking
- **research** — Deep research on any topic via Perplexity Sonar Pro. Saves results to `outputs/research/`.
- **deep-research-consensus** — Spawns multiple parallel agents with varied framings, then aggregates by consensus, divergence, and outliers. Use when one agent isn't enough.
- **agent-debate** — Spawns agents with distinct personalities and has them debate a topic across rounds. Depth instead of breadth.
- **challenge** — Skeptically rip apart a business idea. Built to kill bad ideas early before you waste a week building them.
- **boomer** — Explain any tech/crypto/AI concept in plain language for someone smart but not in the bubble.

### YouTube
- **youtube-outline** — Structured outline of a video so you can decide in 30 seconds whether to watch.
- **youtube-compare** — Compare two videos and surface the actual learning gap between them.
- **youtube-action-steps** — Turn a tutorial video into a step-by-step instruction list (uses Gemini's video understanding).

### Image generation (Gemini API)
- **image-generation-realistic** — Hyper-realistic photo generation with structured JSON prompts that fight the AI "plastic" look.
- **image-generation-brand** — Logos, app icons, flat-vector brand illustrations.
- **image-generation-infographic** — Clean infographics, flowcharts, process diagrams, comparison charts.

### Utility
- **preview** — Render any markdown file as a styled HTML page and open it in the browser.
- **handoff** — Produce a session handoff summary and copy it to clipboard, so you can `/clear` and paste into a fresh session without losing context.

## Install

These live in my Dropbox and are symlinked into `~/.claude/skills/`. Easiest way to use them:

```bash
git clone git@github.com:jelle/claude-skills.git ~/claude-skills
ln -s ~/claude-skills/* ~/.claude/skills/
```

Or copy individual skill folders directly into `~/.claude/skills/`.

## Heads up

A few skills call helper scripts that live in my own workspace, not in this repo:
- `scripts/perplexity_research.py` — for `research` and `deep-research-consensus`
- `scripts/generate_image.py` — for the three `image-generation-*` skills
- `scripts/preview_md.py` — for `preview`
- `scripts/get_youtube_transcript.py` — for `youtube-outline` and `youtube-compare`
- `scripts/video_to_action.py` — for `youtube-action-steps`

You'll need API keys (`PERPLEXITY_API_KEY`, `GEMINI_API_KEY`) and your own versions of these scripts. Nothing fancy — the skills tell Claude what to call, the scripts do the actual work.

A few personal skills (portfolio briefings, LinkedIn voice, etc.) are intentionally gitignored.

## License

MIT. Take what's useful, fork what isn't.
