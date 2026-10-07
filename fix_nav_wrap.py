with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
'''.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  font-size: 0.85rem;
  position: relative;
  padding: 0.5rem 0;
}''', 
'''.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  font-size: 0.85rem;
  position: relative;
  padding: 0.5rem 0;
  white-space: nowrap;
}'''
)

css = css.replace(
'''.dropdown-toggle {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 0.85rem;
  padding: 0.5rem 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}''',
'''.dropdown-toggle {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-body);
  font-weight: 500;
  font-size: 0.85rem;
  padding: 0.5rem 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added white-space: nowrap to nav links.")
