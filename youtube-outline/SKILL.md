---
name: youtube-outline
description: Create a structured outline of a YouTube video so Jelle can quickly decide if it's worth watching and what he'd learn. Use this skill whenever the user shares a YouTube URL and wants a summary, outline, or breakdown, or asks "what's in this video", "is this worth watching", "outline this", or "summarize this video". Also trigger when the user pastes a YouTube link without further instruction — outlining is the default action for YouTube URLs.
---

# YouTube Outline

Extract the key learnings from a YouTube video and present them as a scannable outline, so Jelle can decide in 30 seconds whether to spend 20+ minutes watching.

## Why this format

Jelle learns primarily through YouTube but doesn't have time to watch everything. The outline format lets him triage videos fast: what's the topic, what would he learn, what can he skip. The "Worth watching?" verdict is the most important line.

## Input

$ARGUMENTS = a YouTube URL or video ID.

## Steps

1. Fetch the transcript:
   ```
   python3 ./scripts/get_youtube_transcript.py "$ARGUMENTS" --meta
   ```

2. Fetch video metadata (title, channel) via the YouTube oembed API:
   ```python
   python3 -c "
   import json, urllib.request
   url = 'https://www.youtube.com/oembed?url=$ARGUMENTS&format=json'
   req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
   resp = urllib.request.urlopen(req)
   print(json.dumps(json.loads(resp.read()), indent=2))
   "
   ```

3. Analyze the transcript and produce this outline:

   ### Video Summary
   - **Title**: [from metadata]
   - **Channel**: [from metadata]
   - **Duration**: [from transcript meta]
   - **Topic**: [1-2 sentence summary]
   - **Worth watching?**: [Yes/No/Partially — with reason]

   ### Key Topics Covered
   - [Topic 1] — [brief description]
   - [Topic 2] — [brief description]

   ### What You'd Learn
   - [Concrete takeaway 1]
   - [Concrete takeaway 2]

   ### Notable Tools/Resources Mentioned
   - [Tool/resource and what it does]

   ### Skip Sections
   - [Timestamps or descriptions of filler/intro/sponsor sections]

4. Save the outline to `outputs/youtube/[video-id]-outline.md`

5. If the content is substantive and relates to active learning paths (AI, automation, investment), save key learnings to memory. If the video is investment-related, also extract key insights to `portfolio/knowledge/`.

6. Present the outline in chat.
