with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace background-color: #ffffff; with background-image: linear-gradient(#ffffff, #ffffff) !important;
css = css.replace(
    'background-color: #ffffff;',
    'background-image: linear-gradient(#ffffff, #ffffff) !important; background-color: transparent;'
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with gradient background trick")
