---
name: prime
description: Lightweight session bootstrap — reads CLAUDE.md, memory, and git status. Use when starting a new session without needing full dashboard. Trigger on "prime", "load context", "start session", or "good morning".
---

# Prime

Quick session bootstrap. Loads just enough context to be useful immediately — no API calls, no agent reports, no ASCII diagrams.

## Steps

1. Read `CLAUDE.md` in the project root
2. Read all auto-memory files from the memory directory (scan MEMORY.md for what's there)
3. Run `git log --oneline -10` to see recent work
4. Count actors: `ls actors/ | wc -l` for total, check `docs/actor-status.json` if it exists for published count

## Output

Respond with a brief summary (under 10 lines):
- Current state: total actors, published count, last commit
- Any relevant memories from previous sessions (active priorities, pending work)
- Remind that `/dashboard` is available for the full overview with live stats
- Confirm ready to assist

Be direct and concise. This is the fast-start option.
