with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

bad_block = '''.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  margin-left: auto;
  margin-right: 2rem;
}'''

good_block = '''.nav-menu {
  display: flex;
  align-items: center;
  gap: 2rem;
}'''

css = css.replace(bad_block, good_block)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
