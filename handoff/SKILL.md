---
name: handoff
description: Produce a session-handoff summary and copy it to the clipboard so it can be pasted into a new session after /clear. Use when the user says "handoff", "handoff summary", "summarize session", "prepare for context clear", "copy summary", or indicates they're about to clear context and want to preserve what was just done.
---

# Handoff

Produce a compact handoff summary of the current session, save a dated copy to disk, and put it on the clipboard so the user can paste it into a fresh Claude session after `/clear`.

## Why this exists

Context windows fill up. Many users clear around 15% remaining (per Nate Herk's workflow). A good handoff = new session continues productively instead of starting cold.

## Output format (Standard detail level)

The handoff is written in second-person to future-Claude, not as a status report. Shape:

```markdown
# Session handoff — <YYYY-MM-DD HH:MM>

**Workspace:** <cwd basename>
**Context at handoff:** ~<N>% remaining (approximate)

## What we were doing
<1-3 sentences: the goal of this session in plain terms>

## What got done
- <concrete change 1>
- <concrete change 2>
- ...

## Decisions made
- <decision + one-line rationale>
- ...

## Open questions / not yet decided
- <question 1>
- ...

## Files / systems touched
- `<path>` — <what changed>
- ...

## Next step
<one concrete action the fresh session should take first>

## Pick up by
1. Run `/prime` to load workspace context + memory.
2. Read this handoff.
3. Start with "Next step" above.
```

Keep each section tight. Better short and truthful than long and padded. Omit sections that genuinely have nothing (e.g. "Open questions" if there are none — just drop the heading).

## Steps

1. **Compose the summary** using what you remember from this session. Be concrete — names of files, exact decisions, actual blockers. No fluff like "we had a productive discussion about X."

2. **Save to disk** at `outputs/handoffs/YYYY-MM-DD-HHMM-<slug>.md` where `<slug>` is a 2-4 word kebab-case hint of the topic. Create the directory if it doesn't exist. If the current workspace has no `outputs/` convention, fall back to `~/.claude/handoffs/`.

3. **Copy to clipboard** via `pbcopy < <saved-file>` (macOS). This is the critical step — the user's whole reason for invoking this skill is to paste into a fresh session.

4. **Confirm** in one sentence: where it was saved, that it's on the clipboard, and the filename. Then show the full handoff text back to the user so they can sanity-check before clearing.

5. **Stop.** Do not prompt the user about saving to memory. The user will tell you what to save (e.g. "save X to memory") if anything from this session needs persisting. Don't ask, don't propose — just produce the handoff and end.

## Don't

- Don't skip the clipboard step. That's the whole point.
- Don't ask the user about memory — they'll tell you what to save if anything's worth keeping.
- Don't ask the user to approve the summary before copying — they want it fast. They'll read it after it's on the clipboard and adjust next time if needed.
- Don't include verbatim code blocks in the handoff unless the code itself IS the decision (rare). Reference files by path instead.
- Don't pad. If the session was 3 messages, the handoff is 3 lines.
