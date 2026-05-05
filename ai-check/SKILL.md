---
name: ai-check
description: Scan text for AI writing tells and flag them. Use when user says "ai check", "does this sound like AI", "check for AI", "ai review", "humanize", or wants to verify text doesn't read as machine-generated. Works on any file, selection, or pasted text.
---

# AI Check

Scan text for patterns that make writing read as AI-generated. Flag each issue with the specific line, the problem, and a fix.

## Input

$ARGUMENTS = file path, or empty (use the current selection / most recently discussed text).

If a file path is given, read the file first. If no arguments and no selection context, ask what to check.

## What to flag

### Structural tells

1. **Clipped sentence stacks** — 3+ short sentences back-to-back ("Small groups. Every two weeks. Four hours online."). Fold facts into flowing sentences with commas, "and", or subordinate clauses. One or two short sentences are fine as punchlines; three in a row is a pattern.

2. **Parallel structure repetition** — Same sentence shape used for multiple items in a list or across sections. Real writing varies rhythm. If every type/variant/item follows "Name. What it is. Detail. Qualifier." — that's templated.

3. **Symmetric rhetorical constructions** — "You don't choose X — you choose Y." Clever contrasts that feel written-to-impress rather than written-to-inform. Unless the author talks like that naturally.

4. **Staccato closers** — Punchy short sentence sequences at the end of sections for rhetorical effect ("One tool. One evening. Everything you need."). Dead AI giveaway.

### Vocabulary tells

5. **Banned words** — leverage, delve, unlock, tapestry, synergy, ecosystem, seamless, empower, game-changer, revolutionize, transform, journey, dive deep, elevate, supercharge, navigate (as metaphor), robust, comprehensive, streamline, facilitate, utilize, cutting-edge, innovative, harness, holistic, paradigm.

6. **Banned phrases** — "in today's fast-paced world", "in the ever-evolving landscape", "in the world of", "not just X, but Y", "imagine a world where", "more than ever before", "at its core", "it's worth noting that", "this is where X comes in", "the key takeaway here is".

7. **Corporate passive** — "is supported", "is provided", "can be leveraged", "is utilized". Prefer active voice: "you can", "the system does", "use this when".

8. **Filler qualifiers** — "This is the most common X" as a standalone sentence (adds nothing). "It's important to note that..." (just state the thing). "As mentioned earlier..." (don't self-reference).

9. **Slang and hustle-culture idioms** — "level up", "crush it", "dive in", "game on", "vibes", "no cap", "lowkey", "it hits different", "jack in". AI uses these trying to sound casual. Real professional copy doesn't.

10. **Exclamation marks** — AI adds these for fake enthusiasm. Professional and technical copy almost never needs them. Flag every one.

11. **Emojis in body copy** — AI scatters emojis to appear friendly. Unless the format explicitly calls for them (social media captions, chat), flag them.

### Tone tells

12. **Overwritten descriptions** — "a carefully orchestrated mechanism that provides users with real-time visual feedback" when "shows a live preview" says the same thing in four words. If a description works harder than the concept requires, trim it.

13. **Fake hedging** — "It might be worth considering..." when the text is clearly recommending. Say it directly.

14. **Em-dash overuse** — More than 2 em-dashes per page is a tell. Use periods, commas, or line breaks. (Note: em-dashes are fine in technical specs where they separate name from description.)

15. **Transition words that sound essay-like** — "Furthermore,", "Moreover,", "Consequently,", "Concretely,", "Additionally,". Drop or rewrite the sentence without them.

16. **"Align with" / "ensure" / "facilitate"** — Corporate-speak. "Match", "make sure", "help" are human equivalents.

## How to report

For each issue found:

```
L[line] — [category]
"[the flagged text]"
→ [why it's a problem + suggested fix]
```

Group by severity:
1. **Hard tells** — would trip an AI detector or immediately read as machine-generated
2. **Soft tells** — wouldn't trip a detector alone but contribute to an AI "feel" when combined
3. **Style notes** — not strictly AI tells but worth flagging for naturalness

## After the scan

- Report total count: "X issues found (Y hard, Z soft, W style)"
- If the text is clean: say so, don't invent problems
- Offer to fix all issues in one pass if user wants

## What NOT to flag

- Technical terminology used correctly (API names, design system terms, framework concepts)
- Lists and tables — structured formats are fine in documentation and guidelines
- Short sentences used as section openers or punchlines (only flag stacks of 3+)
- Em-dashes in anatomy tables or spec sheets where they serve as separators
