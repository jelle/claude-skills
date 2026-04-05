---
name: preview
description: Render a markdown file as a clean, readable HTML page and open it in the browser. Use when the user says "preview", "show me", "render", "read this nicely", or wants to view any .md file in a more readable format.
---

# Preview

Render a markdown file as a styled HTML page and open it in the browser for comfortable reading.

## Input

$ARGUMENTS = a path to a markdown file (relative or absolute).

## Steps

1. Read the markdown file at the given path. If no path is given, ask which file to preview.

2. Convert the markdown content to a styled HTML page using this Python script:
   ```
   python3 ./scripts/preview_md.py "<file_path>"
   ```

3. The script will open the HTML in the default browser automatically.

4. Confirm to the user that the preview is open.
