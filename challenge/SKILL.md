---
name: challenge
description: Skeptically challenge any business idea, opportunity, or plan. Use this skill when the user presents a business idea and wants honest feedback, says "what do you think of this idea", "is this worth building", "challenge this", "tear this apart", "reality check", or when they describe a new venture and you sense they'd benefit from a critical assessment before investing time. Better to kill a bad idea early than waste weeks building it.
---

# Challenge

Rip apart business ideas with constructive skepticism. The goal is to find fatal flaws early — before you spend weeks building something that won't work.

## Why this exists

Ideas sound good in your head but often fall apart under scrutiny. This skill pressure-tests a new idea against market reality, competitor presence, revenue math, and risk factors — so the same mistakes don't get repeated.

## Input

$ARGUMENTS = the idea or opportunity to challenge.

## Analysis Framework

0. **Load project context FIRST** — before any analysis, you MUST:
   - Read `MEMORY.md` from the auto-memory directory to understand what's already known
   - Read ALL memory files relevant to the idea being challenged (decisions, feedback, project status, infrastructure, revenue data, user preferences)
   - Read `CLAUDE.md` in the project root (if it exists) for project-specific instructions
   - Read any other project docs referenced in memory that relate to the topic
   - Understand what systems, tools, and processes are already in place — NEVER claim something is missing without verifying against the actual codebase and memory
   
   **Why:** Challenges based on incorrect assumptions about the project state are worse than useless — they waste time and erode trust. Know the facts before making claims. The memory system exists precisely so that context carries across sessions — use it.

1. Read the idea. If it references a file in `ideas/`, read that file for context.

2. Run a skeptical analysis covering these angles:

   ### Market Reality
   - How big is the actual addressable market? (not TAM fantasy — real buyers who'd pay)
   - What comparable products/services exist? Search Apify Store, web, etc.
   - If competitors exist: user counts, ratings, success rates?
   - If no competitors: is that because there's no demand?

   ### The "Why hasn't anyone done this?" Test
   - If the gap is obvious, why is it still a gap?
   - Is the incumbent who SHOULD have built this choosing not to? That's a signal.
   - Is the problem actually hard (anti-bot, legal, maintenance)?

   ### Revenue Reality Check
   - Build a pessimistic / realistic / optimistic revenue table
   - Factor in actual costs (proxies, compute, maintenance time)
   - Compare effort-to-revenue ratio against alternatives

   ### Demand Validation
   - Is there PROVEN demand (user counts, search volume, Reddit threads)?
   - Or is demand assumed from "this site has lots of traffic"?
   - Would potential buyers pay, or do free/cheap alternatives exist?

   ### Risk Factors
   - Legal risks (ToS violations, GDPR, cease & desist)
   - Technical risks (anti-bot, maintenance burden, site changes)
   - Competitive risks (someone better-funded enters the market)
   - Timing risks (is this opportunity growing or shrinking?)

   ### The KBO Test (named after a killed idea)
   - Is the data freely available elsewhere? (free APIs, bulk downloads, public datasets)
   - Does a scraper actually solve an ACCESS problem, or just a CONVENIENCE problem?

3. Use `/research` (Perplexity) for any factual claims that need verification. Don't trust assumptions.

4. Verify all competitor claims against the actual Apify Store (search-actors tool). Perplexity frequently gets Apify Store data wrong.

5. Deliver a clear verdict:
   - **BUILD** — opportunity is real, defensible, and worth the effort
   - **CONDITIONAL** — could work IF [specific conditions]
   - **SKIP** — not worth the effort, here's why
   - **PIVOT** — the core insight is good but the execution should be different (explain how)

6. If verdict is SKIP or PIVOT, suggest what to do instead.

## Tone

Be direct. Don't soften bad news — better to kill a bad idea early. But also be fair — acknowledge genuine strengths before tearing them down.
