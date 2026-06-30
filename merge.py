import re
import os

index_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\index.html"
code_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\temp_stitch\code.html"
main_js_path = r"c:\Users\rohit\Desktop\PYTHON DEVS DRINK\scroll_animation\main.js"

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

with open(code_path, 'r', encoding='utf-8') as f:
    code_html = f.read()

# Extract head from code.html
head_match = re.search(r'(<script src="https://cdn.tailwindcss.com.*?</style>)', code_html, re.DOTALL)
if head_match:
    head_content = head_match.group(1)
    # Insert into index.html head
    index_html = index_html.replace('</head>', head_content + '\n</head>')

# Add html class
index_html = index_html.replace('<html lang="en">', '<html lang="en" class="dark">')

# Add body class
index_html = index_html.replace('<body>', '<body class="antialiased selection:bg-primary-container selection:text-on-primary-container">')

# Extract sections from code.html
sections_match = re.search(r'(<!-- Intro & Story -->.*</footer>)', code_html, re.DOTALL)
if sections_match:
    sections_content = sections_match.group(1)
    # Insert before <script src="main.js">
    index_html = index_html.replace('<script src="main.js"></script>', sections_content + '\n    <script src="main.js"></script>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)

# Extract JS
js_match = re.search(r'<script>\s*(// Simple Intersection Observer.*?)\s*</script>\s*</body>', code_html, re.DOTALL)
if js_match:
    js_content = js_match.group(1)
    with open(main_js_path, 'a', encoding='utf-8') as f:
        f.write('\n\n' + js_content + '\n')
