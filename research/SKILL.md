---
name: research
description: Deep research on any topic using the Perplexity Sonar Pro API. Use this skill when the user asks to research something, wants in-depth information on a topic, says "look into", "deep dive", "research this", "what's the landscape for", or needs comprehensive, sourced information beyond what a quick web search provides. Saves results to outputs/research/ for future reference.
---

# Deep Research

Use the Perplexity API (Sonar Pro) to do thorough research on any topic and present clean, actionable findings.

## Why Perplexity

Web search gives headlines. Perplexity Sonar Pro synthesizes across multiple sources and provides cited, comprehensive answers. At ~$0.01 per query, it's the best cost/quality ratio for research that needs to be reliable.

## Input

$ARGUMENTS = the research question or topic.

## Steps

0. **Load project context FIRST** — before running any research, you MUST:
   - Read `MEMORY.md` from the auto-memory directory to understand what's already known about this topic
   - Read any memory files relevant to the research question
   - Read `CLAUDE.md` in the project root (if it exists) for project-specific instructions
   - Check if prior research already exists in `outputs/research/` that covers the same or overlapping topic
   - Use this context to craft better Perplexity queries and avoid re-researching what we already know
   
   **Why:** Research without project context produces generic answers that ignore what's already been decided or discovered. Context-aware research builds on existing knowledge instead of repeating it. The memory system exists precisely so that context carries across sessions — use it.

1. Generate a short topic slug from the question (e.g., "apify actor opportunities" → "apify-actor-opportunities").

2. Run the Perplexity research script with sonar-pro for maximum depth:
   ```
   python3 scripts/perplexity_research.py "$ARGUMENTS" --model sonar-pro --save "outputs/research/[YYYY-MM-DD]-[short-topic-slug].md"
   ```

3. Read the saved output file.

4. Present a clean summary:
   - Key findings (bullet points, concise)
   - Actionable takeaways
   - Sources used
   - Where the full output was saved

5. If the research connects to an existing idea in `ideas/` or an active project in `projects.md`, mention the connection and offer to update that file.

6. If the user asks to remember or save findings, update the relevant memory or ideas files.

## Model Options

The script supports multiple models. Default is sonar-pro (best quality).
- `sonar` — cheaper, faster, good for quick lookups
- `sonar-pro` — deep research, comprehensive (default)
- `sonar-reasoning` — step-by-step reasoning
- `sonar-reasoning-pro` — deepest reasoning

## Examples

- `/research what are the most profitable Apify actor niches in 2026`
- `/research real estate market data sources and APIs`
- `/research EU web scraping legal landscape GDPR compliance 2026`
