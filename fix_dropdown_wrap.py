with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
'''.nav-dropdown-item {
  display: block;
  padding: 0.75rem 1.25rem;
  color: rgba(255, 255, 255, 0.85);
  font-size: 0.9rem;
  font-weight: 500;
  transition: var(--transition);
  text-align: center;
}''',
'''.nav-dropdown-item {
  display: block;
  padding: 0.75rem 1.25rem;
  color: rgba(255, 255, 255, 0.85);
  font-size: 0.9rem;
  font-weight: 500;
  transition: var(--transition);
  text-align: center;
  white-space: nowrap;
}'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added white-space: nowrap to dropdown items.")
