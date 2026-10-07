with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Nav Menu
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

# Nav Link
old_link = '''.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  font-size: 1.05rem;'''
new_link = '''.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  font-size: 1.15rem;'''
css = css.replace(old_link, new_link)

# Lang Btn
old_lang = '''.lang-btn {
  white-space: nowrap;
  font-size: 1.05rem;'''
new_lang = '''.lang-btn {
  white-space: nowrap;
  font-size: 1.15rem;'''
css = css.replace(old_lang, new_lang)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied precise patch.")
