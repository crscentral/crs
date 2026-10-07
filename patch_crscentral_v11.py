import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('font-size: 1.15rem;', 'font-size: 1.25rem;')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated font size to 1.25rem")
