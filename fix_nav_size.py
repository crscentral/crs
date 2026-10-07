with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Restore .nav-link
css = css.replace(
'''  font-size: 0.85rem;
  position: relative;
  padding: 0.5rem 0;
  white-space: nowrap;
}
''',
'''  font-size: 0.95rem;
  position: relative;
  padding: 0.5rem 0;
  white-space: nowrap;
}
''')

# 2. Restore .nav-menu
css = css.replace(
'''.nav-menu {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-left: auto;
  margin-right: 1rem;
}''',
'''.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-left: auto;
  margin-right: 2rem;
}''')

# 3. Restore .dropdown-toggle
css = css.replace(
'''  font-size: 0.85rem;
  padding: 0.5rem 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;''',
'''  font-size: 0.95rem;
  padding: 0.5rem 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;''')

# 4. Restore .lang-btn
css = css.replace(
'''.lang-btn {
  white-space: nowrap;
  font-size: 0.85rem;
  background: transparent;''',
'''.lang-btn {
  white-space: nowrap;
  font-size: 0.95rem;
  background: transparent;''')

# Also fix the other instance of lang-btn padding if needed, but let's do a simple regex or string replace.
css = css.replace("font-size: 0.85rem;", "font-size: 0.95rem;")

# But wait, there are other elements using 0.85rem! 
# Let's revert the blanket replace and do targeted ones.
