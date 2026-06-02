---
name: copy
description: Copy file contents to clipboard. Use when user says "copy", "clipboard", "copy to clipboard", "pbcopy", or wants to paste file contents somewhere else.
---

# Copy

Copy the contents of a file to the system clipboard.

## Input

$ARGUMENTS = file path (relative or absolute).

## Steps

1. If no path given, ask which file to copy.

2. Read the file to confirm it exists.

3. Copy to clipboard:
   ```
   pbcopy < "<file_path>"
   ```

4. Confirm: file name, line count, and that it's on the clipboard.
