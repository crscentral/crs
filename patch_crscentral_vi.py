import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('@media (min-width: 1301px) {\n  html[lang="vi"] .header-container', '@media (min-width: 1001px) {\n  html[lang="vi"] .header-container')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied Vietnamese breakpoint fix.")
