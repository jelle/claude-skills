---
name: youtube-action-steps
description: Extract step-by-step action instructions from a YouTube tutorial video using Gemini's video understanding. Use when the user says "learn from this video", "extract steps from this video", "replicate this tutorial", "youtube action steps", "action steps", or wants to turn a video tutorial into executable instructions.
---

# YouTube Action Steps

Turn a YouTube tutorial into a hyper-detailed step-by-step breakdown that another AI agent (or you) can follow to replicate the tutorial.

## How it works

1. Sends the YouTube URL directly to Gemini's video understanding API
2. Gemini watches the full video and extracts every action, click, and configuration
3. Returns structured steps with timestamps, UI elements, and exact values

## Input

$ARGUMENTS = a YouTube URL.

## Steps

1. Run the extraction script:
   ```
   python3 ./scripts/video_to_action.py "$ARGUMENTS" --save "./outputs/youtube/$VIDEO_ID-action-steps.md"
   ```
   Where `$VIDEO_ID` is extracted from the YouTube URL.

2. Read the generated file.

3. Present a summary to the user:
   - What the tutorial teaches
   - Tools/platforms used
   - Number of steps extracted
   - Ask if they want you to execute any of the steps

4. If the user wants to execute the steps, use the extracted instructions as your guide. Open browsers, click buttons, run commands — whatever the tutorial showed.

## Notes

- Requires `GOOGLE_API_KEY` in `.env` (Google AI Studio)
- Uses Gemini 2.5 Flash for video understanding
- No video download needed — sends URL directly to Gemini
- Works best on tutorials under 30 minutes. Longer videos may need to be split.
