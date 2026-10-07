with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the specific header-container block
old_header = '''.header-container {
  max-width: 1200px;
  height: 100%;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}'''

new_header = '''.header-container {
  max-width: 1350px;
  height: 100%;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}'''

css = css.replace(old_header, new_header)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated header-container max-width.")
