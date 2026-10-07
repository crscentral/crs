with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_dropdown = '''.dropdown-toggle {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 0.95rem;'''
new_dropdown = '''.dropdown-toggle {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 1.15rem;'''
css = css.replace(old_dropdown, new_dropdown)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied dropdown font patch.")
