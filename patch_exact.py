with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. header-container
old_header = '''.header-container {
  max-width: 1200px;
  height: 100%;'''
new_header = '''.header-container {
  max-width: 1440px;
  height: 100%;'''
css = css.replace(old_header, new_header)

# 2. nav-menu
old_nav = '''.nav-menu {
  display: flex;
  align-items: center;
  gap: 2rem;
}'''
new_nav = '''.nav-menu {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: space-evenly;
  margin: 0 2rem;
}'''
css = css.replace(old_nav, new_nav)

# 3. nav-link
old_link = '''.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  font-size: 0.95rem;
  position: relative;'''
new_link = '''.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  font-size: 1.05rem;
  position: relative;'''
css = css.replace(old_link, new_link)

# 4. lang-btn
old_lang = '''.lang-btn {
  padding: 0.5rem 1rem;
  white-space: nowrap;
  background: transparent;'''
new_lang = '''.lang-btn {
  padding: 0.5rem 1rem;
  white-space: nowrap;
  font-size: 1.05rem;
  background: transparent;'''
css = css.replace(old_lang, new_lang)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Exact patch applied.")
