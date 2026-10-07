with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix social icon hover
css = css.replace(
    '''.social-icon:hover {
  color: var(--accent-color);
  background-image: linear-gradient(#ffffff, #ffffff) !important; background-color: transparent;
  border-color: #ffffff;''',
    '''.social-icon:hover {
  color: var(--accent-color);
  background-color: #ffffff;
  border-color: #ffffff;'''
)

# Fix whatsapp badge
css = css.replace(
    '''.whatsapp-badge {
  position: absolute;
  right: 75px;
  background-image: linear-gradient(#ffffff, #ffffff) !important; background-color: transparent;
  color: #128c7e;''',
    '''.whatsapp-badge {
  position: absolute;
  right: 75px;
  background-color: #ffffff;
  color: #128c7e;'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted unintended gradient replacements")
