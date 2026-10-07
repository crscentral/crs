with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    'filter: brightness(0) invert(1); /* Forces logo color to solid white */',
    '''background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center left;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center left;'''
)

css = css.replace(
    'filter: brightness(0) invert(1) opacity(0.85); /* Premium hover feedback */',
    'opacity: 0.85;'
)

# And fix width
css = css.replace(
    '''.calc-header-logo {
  display: block;
  height: 38px;
  width: auto;''',
    '''.calc-header-logo {
  display: block;
  height: 38px;
  width: 120px;'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css")
