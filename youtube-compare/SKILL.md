---
name: youtube-compare
description: Compare two YouTube videos to find the learning gap — what new stuff the second one covers that the first didn't. Use this skill when the user provides two YouTube URLs and wants a comparison, asks "what's different between these", "should I watch both", "compare these videos", or wants to know if a second video is worth watching after already seeing the first.
---

# YouTube Compare

Compare two YouTube videos side by side to find the learning gap — the unique value in each that the other doesn't cover. Helps you decide if a second video on a similar topic is worth the time.

## Why this exists

When you watch a lot of YouTube content on similar topics (AI, crypto, automation, etc.), many videos cover the same ground. This skill identifies what's genuinely new in each video so you can skip redundant content and only watch the parts that add to your knowledge.

## Input

$ARGUMENTS = two YouTube URLs, space-separated.

## Steps

1. Parse the two URLs from the input. If only one is given, ask for the second.

2. Fetch both transcripts:
   ```
   python3 ./scripts/get_youtube_transcript.py <url1> --meta
   python3 ./scripts/get_youtube_transcript.py <url2> --meta
   ```

3. Fetch video metadata for both via the YouTube oembed API.

4. Analyze both transcripts and produce this comparison:

   ### Videos Compared
   - **Video A**: [title] ([duration])
   - **Video B**: [title] ([duration])

   ### Overlapping Topics
   - [Topics both videos cover, with notes on which explains better]

   ### Unique to Video A
   - [Topics only covered in Video A]

   ### Unique to Video B (The Learning Gap)
   - [Topics only in Video B — THIS is what you'd gain by watching it]

   ### Recommendation
   - [Should I watch Video B? Full watch or skip to specific parts?]
   - [Specific sections/timestamps to focus on if partial watch]

   ### Combined Takeaways
   - [Top 5 actionable insights from both videos together]

5. Save the comparison to `outputs/youtube/compare-[videoA-id]-vs-[videoB-id].md`

6. Save any new learnings to memory.

7. Present the comparison in chat.
