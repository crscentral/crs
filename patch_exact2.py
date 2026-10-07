with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_lang = '''.lang-btn {
  white-space: nowrap;
  font-size: 0.95rem;'''
new_lang = '''.lang-btn {
  white-space: nowrap;
  font-size: 1.05rem;'''

css = css.replace(old_lang, new_lang)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
