---
name: deep-research-consensus
description: Spawn multiple parallel agents with varied analytical framings to research a question, then aggregate results by consensus, divergence, and outliers. Use when the user says "consensus research", "deep agent research", "stochastic research", "parallel research", "scan the search space", "multi-agent research", or wants a more thorough answer than a single agent can provide. Also trigger when the user asks a strategic question and mentions wanting "multiple perspectives" or "different angles".
---

# Deep Research Consensus

Exploit stochasticity by spawning parallel agents with varied framings to scan a much larger portion of the solution space than a single query ever could. Then aggregate by consensus, divergence, and outliers.

## Why this works

A single agent query covers maybe 15-20% of the possible answer space. By spawning N agents with slightly different analytical framings, we statistically traverse 60-80% of the space. Consensus items are high-confidence. Outliers are potential breakthroughs that only surface 5-10% of the time.

## Input

$ARGUMENTS = the question, problem, or topic to research deeply.

## Steps

0. **Load project context FIRST** — before spawning any agents, you MUST:
   - Read `MEMORY.md` from the auto-memory directory to understand what's already known
   - Read ALL memory files that are relevant to the research topic (decisions, feedback, project status, infrastructure, user preferences)
   - Read `CLAUDE.md` in the project root (if it exists) for project-specific instructions
   - Read any other project docs referenced in memory that relate to the topic
   - Compile a **Context Brief** (bullet points) summarizing: what systems/tools/processes are already in place, what has been tried, what decisions have been made, current state/metrics, and any relevant user feedback or preferences
   - This Context Brief MUST be included in every agent's prompt so they research from facts, not assumptions
   
   **Why:** Agents that research without project context make uninformed claims about things that are already solved, contradict decisions already made, or propose solutions that already exist. This wastes time and erodes trust. The memory system exists precisely so that context carries across sessions — use it.

1. **Analyze the question** and determine:
   - Is this a strategic/ideation question (use 7 agents) or a factual/analytical question (use 5 agents)?
   - What kind of framing variations would produce the most diverse responses?

2. **Design framing variations**. Each agent gets the same core question but with a different analytical lens. Examples:
   - Conservative/risk-focused analysis
   - Optimistic/opportunity-focused analysis
   - Contrarian/devil's advocate
   - First-principles reasoning
   - Pattern-matching from analogous domains
   - End-user/customer perspective
   - Data-driven/quantitative lens
   - Time-horizon variations (short-term vs long-term)
   - Resource-constrained perspective (what if budget is tight?)
   - Geographic/cultural lens (regional, country-specific, etc.)

3. **Spawn all agents in parallel** using the Agent tool. Each agent should:
   - Receive the **Context Brief** from step 0 (MANDATORY — agents must know the project state)
   - Receive the core question + its unique framing instruction
   - Be told: "Read the Context Brief carefully — these are FACTS about the project. Do not contradict them or assume things that conflict with them."
   - Be told to produce 3-5 concrete, specific answers/ideas/recommendations
   - Use web search if the question requires current data
   - Return structured output: numbered list with brief reasoning per item

   Use `subagent_type: "general-purpose"` for each. All agents launch in a single message for true parallelism.

4. **Aggregate results** once all agents return. Build a consensus report:

   ### Consensus Report: [Topic]

   **Question**: [the original question]
   **Agents spawned**: [N]
   **Framing variations used**: [list them]

   #### Consensus (appeared in 60%+ of agents)
   - [Item] — appeared in N/N agents. [Why this has high confidence]

   #### Strong signals (appeared in 30-60% of agents)
   - [Item] — appeared in N/N agents. [Context]

   #### Divergent (agents disagreed)
   - [Item] — [Agent A says X, Agent B says Y]. [What drives the disagreement]

   #### Outliers (appeared in 1-2 agents only)
   - [Item] — [Which framing produced this]. [Why it might be brilliant or why it might be noise]

   #### Synthesis
   - [2-3 sentences combining the strongest consensus items with the most promising outliers into an actionable recommendation]

5. **Save the report** to `outputs/research/[YYYY-MM-DD]-consensus-[topic-slug].md`

6. Present the report in chat, highlighting the outliers — those are the ideas you wouldn't have found with a single query.

## Cost

Roughly $0.10-0.30 per run depending on agent count and whether web search is used. Cheap for the breadth of analysis you get.

## Examples

- `/deep-research-consensus What's the best monetization model for a niche consumer app?`
- `/deep-research-consensus How should a UX designer position themselves in an AI-first job market?`
- `/deep-research-consensus What Chrome extension niches are currently underserved?`
