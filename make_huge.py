with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make font sizes HUGE
css = css.replace('font-size: 1.05rem;', 'font-size: 1.2rem;')

# Revert nav-menu to use gap but HUGE gap
old_nav = '''.nav-menu {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: space-evenly;
  margin: 0 2rem;
}'''
new_nav = '''.nav-menu {
  display: flex;
  align-items: center;
  gap: 3rem;
}'''
css = css.replace(old_nav, new_nav)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied HUGE fonts and gaps.")
