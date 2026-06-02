---
name: prime
description: Lightweight session bootstrap — picks up any pending handoff, reads CLAUDE.md, loads the memory index, and checks workspace status. Use when starting a new session. Trigger on "prime", "load context", "start session", or "good morning".
---

# Prime

Fast session bootstrap. Pick up any pending handoff, orient to the workspace, load the memory index, and report status. Everything else gets lazy-loaded when the conversation touches that topic.

## Steps

0. **Handoff pickup (always run first):**
   - Check whether `.claude/handoff.md` exists in the project root.
   - If yes: read it, note its mtime, delete it (`rm .claude/handoff.md`). One-shot — never let a stale handoff bleed into a later session.
   - If no: cold start.
   - Always report which happened in the final output — the user can't otherwise tell whether `/handoff` did its job last session.

1. **Read `CLAUDE.md`** in the project root (if it exists). This is the workspace's own instructions.

2. **Load memory index:**
   - Read the `MEMORY.md` file from this workspace's auto-memory directory. The auto-memory directory is at `~/.claude/projects/<encoded-cwd>/memory/` where `<encoded-cwd>` is the working directory path with slashes replaced by dashes.
   - If no `MEMORY.md` exists yet, note that this is a fresh workspace with no memory. Don't create one — the auto-memory system handles that when the user asks to remember something.
   - Do NOT eagerly read every memory file. The index has pointers — follow them on demand as the conversation touches those topics.

3. **Workspace status:**
   - If git repo: `git log --oneline -10` + `git status --short`.
   - If not: `ls` the root.

## Lazy-load rule

When the conversation shifts to a new topic:
- If the topic appears in the MEMORY.md pointer list, read that specific memory file.
- If the topic lives in a different workspace (mentioned in the memory index), read that workspace's MEMORY.md, then follow its pointers.

This keeps the prime footprint small without losing context.

## Output

Under 10 lines. Lead with handoff status so continuity is obvious.

- **Handoff status** (one line, always first):
  - Picked up: `Handoff picked up (staged <HH:MM>). Continuing: <one-line summary>.`
  - Cold: `No pending handoff — cold start.`
- Workspace name + purpose (from CLAUDE.md or directory name)
- Key context from the memory index: active priorities, recent decisions
- Fresh workspace → mention it
- End: jump to handoff's "Next step" if picked up, else `Ready to assist.`
