#!/usr/bin/env python3
"""Convert a markdown or plain text file to styled HTML and open in browser."""

import sys
import os
import subprocess
import tempfile
import re

def convert_markdown(content):
    lines = content.split('\n')
    html_parts = []
    in_list = False
    in_code = False
    in_table = False
    table_rows = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Fenced code blocks
        if stripped.startswith('```'):
            if in_code:
                html_parts.append('</code></pre>')
                in_code = False
            else:
                if in_list:
                    html_parts.append('</ul>')
                    in_list = False
                lang = stripped[3:].strip()
                html_parts.append(f'<pre><code class="{lang}">')
                in_code = True
            i += 1
            continue

        if in_code:
            escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html_parts.append(escaped)
            i += 1
            continue

        # Tables
        if '|' in stripped and stripped.startswith('|'):
            if not in_table:
                if in_list:
                    html_parts.append('</ul>')
                    in_list = False
                in_table = True
                table_rows = []
            table_rows.append(stripped)
            i += 1
            continue
        elif in_table:
            html_parts.append(render_table(table_rows))
            in_table = False

        # Empty line
        if not stripped:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append('')
            i += 1
            continue

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            level = len(heading_match.group(1))
            text = inline_format(heading_match.group(2))
            html_parts.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        # ALL-CAPS headers (plain text files)
        if re.match(r'^[A-Z][A-Z &/]+(\s*\[.*\])?$', stripped) and len(stripped) < 60:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append(f'<h2>{stripped}</h2>')
            i += 1
            continue

        # Blockquotes
        if stripped.startswith('> '):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            quote_text = inline_format(stripped[2:])
            html_parts.append(f'<blockquote>{quote_text}</blockquote>')
            i += 1
            continue

        # Horizontal rules
        if re.match(r'^[-*_]{3,}$', stripped):
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            html_parts.append('<hr>')
            i += 1
            continue

        # List items
        if re.match(r'^[-*+]\s', stripped):
            if not in_list:
                html_parts.append('<ul>')
                in_list = True
            item_text = inline_format(re.sub(r'^[-*+]\s', '', stripped))
            html_parts.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', stripped):
            if not in_list:
                html_parts.append('<ol>')
                in_list = True
            item_text = inline_format(re.sub(r'^\d+\.\s', '', stripped))
            html_parts.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Paragraph
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        html_parts.append(f'<p>{inline_format(stripped)}</p>')
        i += 1

    if in_list:
        html_parts.append('</ul>')
    if in_table:
        html_parts.append(render_table(table_rows))

    return '\n'.join(html_parts)


def render_table(rows):
    if len(rows) < 2:
        return ''

    parts = ['<table>']

    # Header
    headers = [c.strip() for c in rows[0].strip('|').split('|')]
    parts.append('<thead><tr>')
    for h in headers:
        parts.append(f'<th>{inline_format(h)}</th>')
    parts.append('</tr></thead>')

    # Body (skip separator row)
    parts.append('<tbody>')
    for row in rows[2:]:
        cells = [c.strip() for c in row.strip('|').split('|')]
        parts.append('<tr>')
        for c in cells:
            parts.append(f'<td>{inline_format(c)}</td>')
        parts.append('</tr>')
    parts.append('</tbody></table>')

    return '\n'.join(parts)


def inline_format(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code class="inline">\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text


STYLE = """
body {
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', system-ui, sans-serif;
    max-width: 720px;
    margin: 48px auto;
    padding: 0 24px;
    line-height: 1.65;
    color: #1d1d1f;
    background: #fafafa;
}
h1 { font-size: 28px; font-weight: 700; margin: 0 0 8px; }
h2 {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: #00915A;
    margin-top: 48px;
    margin-bottom: 8px;
    padding-bottom: 8px;
    border-bottom: 1px solid #e5e5e5;
}
h3 { font-size: 16px; font-weight: 600; margin: 28px 0 6px; color: #333; }
h4 { font-size: 14px; font-weight: 600; margin: 20px 0 4px; color: #444; }
p { margin: 8px 0; font-size: 15px; }
ul, ol { margin: 8px 0; padding-left: 22px; }
li { font-size: 15px; margin: 4px 0; }
blockquote {
    margin: 16px 0;
    padding: 12px 16px;
    border-left: 3px solid #00915A;
    background: #f0f7f4;
    color: #333;
    font-size: 15px;
}
pre {
    background: #f5f5f7;
    border-radius: 8px;
    padding: 16px;
    overflow-x: auto;
    font-size: 13px;
    line-height: 1.5;
}
code.inline {
    background: #f0f0f2;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 13px;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 14px;
}
th, td {
    text-align: left;
    padding: 8px 12px;
    border-bottom: 1px solid #e5e5e5;
}
th { font-weight: 600; background: #f5f5f7; }
hr { border: none; border-top: 1px solid #e5e5e5; margin: 32px 0; }
a { color: #00915A; text-decoration: none; }
a:hover { text-decoration: underline; }
strong { font-weight: 600; }
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: preview_md.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip YAML frontmatter
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            content = content[end + 3:].lstrip('\n')

    # Extract title from first heading or filename
    title_match = re.match(r'^#\s+(.+)', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    else:
        title = os.path.splitext(os.path.basename(file_path))[0]

    body = convert_markdown(content)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{STYLE}</style>
</head>
<body>
{body}
</body>
</html>"""

    out_path = os.path.join(tempfile.gettempdir(), 'claude-preview.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    subprocess.run(['open', out_path])
    print(out_path)


if __name__ == '__main__':
    main()
