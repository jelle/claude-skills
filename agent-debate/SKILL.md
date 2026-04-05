---
name: agent-debate
description: Spawn agents with distinct personalities to debate a topic through multiple rounds, producing sharper and more nuanced analysis than parallel independent research. Use when the user says "debate this", "agent debate", "model chat", "have agents argue about", "stress test this idea", or wants to deeply pressure-test a strategy, decision, or plan through adversarial discussion. Best for decisions where nuance matters more than breadth.
---

# Agent Debate

Spawn agents with distinct personalities and have them debate a topic through structured rounds. Unlike consensus research (breadth), debate produces depth — sharper reasoning, exposed assumptions, and battle-tested conclusions.

## Why this works

Independent parallel agents scan breadth. Debate agents sharpen depth. When agents challenge each other's assumptions, the surviving ideas are much stronger. Weak ideas get killed in the crossfire. Hidden assumptions get exposed. Edge cases get surfaced that no single agent would think of.

## When to use debate vs consensus

- **Consensus** (`/deep-research-consensus`): "What are all the possible approaches?" — breadth, ideation, scanning
- **Debate** (`/agent-debate`): "Which approach is actually best and why?" — depth, stress-testing, decision-making

## Input

$ARGUMENTS = the topic, question, or decision to debate.

## Steps

1. **Analyze the topic** and select 5 debate personas that will produce the most productive friction. Default set:
   - **Systems Thinker** — sees interconnections, second-order effects, feedback loops
   - **Pragmatist** — what actually works in practice? What's the simplest path?
   - **Edge Case Finder** — what breaks this? What's the worst case? What did everyone overlook?
   - **User Advocate** — how does the end user/customer actually experience this?
   - **Contrarian** — deliberately argues the opposite position, challenges consensus

   Adjust personas to fit the topic. For investment questions, swap in a Risk Analyst and a Macro Strategist. For product ideas, swap in a Market Realist and a Growth Hacker.

2. **Run 3 debate rounds** sequentially. Each round, spawn all 5 agents in parallel with:
   - The original topic
   - Their persona description and instruction to stay in character
   - The debate history so far (empty for round 1)
   - Instruction: "Read the previous arguments. Respond in 2-3 paragraphs. You MUST challenge at least one point from another agent. Build on what's strong, attack what's weak. Be specific — no vague agreement."

   After each round, collect all responses and append to the debate history before starting the next round.

   Use `subagent_type: "general-purpose"` for each agent.

3. **Synthesize after round 3**. Analyze the full debate and produce:

   ### Debate Report: [Topic]

   **Topic**: [the original question]
   **Personas**: [list with one-line descriptions]
   **Rounds**: 3

   #### Points of Agreement
   - [What all or most agents converged on after debate]

   #### Key Tensions
   - [Where agents remained in disagreement and why — these are the real decision points]

   #### Assumptions Exposed
   - [Things that were assumed but challenged during debate]

   #### Strongest Arguments
   - [The 2-3 arguments that survived all challenges]

   #### Verdict
   - [Clear recommendation based on which arguments won the debate, with caveats from the dissenting views]

4. **Save the full debate** (all rounds + synthesis) to `outputs/research/[YYYY-MM-DD]-debate-[topic-slug].md`

5. Present the synthesis in chat. Keep the full debate log in the saved file for reference.

## Cost

Roughly $0.15-0.40 per run (5 agents x 3 rounds = 15 agent calls). Worth it for high-stakes decisions.

## Examples

- `/agent-debate Should I build a schema therapy quiz as a website or native iOS app?`
- `/agent-debate Is agent-readiness for SMEs a real market or too early?`
- `/agent-debate Should I rotate SBET profits into MSTR now or wait for a higher multiple?`
