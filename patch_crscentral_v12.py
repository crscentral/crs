import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_nav = '''.nav-menu {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: space-between;
  margin: 0 3rem;
}'''

new_nav = '''.nav-menu {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: space-evenly;
  margin: 0;
}'''

css = css.replace(old_nav, new_nav)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied space-evenly and removed margin")
