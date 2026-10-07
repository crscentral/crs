with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    'filter: brightness(0) invert(1); /* White fonts logo on dark background */',
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

# For the footer logo:
css = css.replace(
    'filter: brightness(0) invert(1); /* White fonts logo in dark footer */',
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

# For the hero logo we probably want center position
css = css.replace(
    '''.hero-logo-img {
  height: 160px;
  width: auto;
  object-fit: contain;
  display: block;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center left;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center left;
}''',
    '''.hero-logo-img {
  height: 160px;
  width: 350px;
  max-width: 100%;
  display: block;
  margin: 0 auto;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center;
}'''
)

# For header logo we need to ensure it has width
css = css.replace(
    '''.logo-img {
  height: 48px;
  width: auto;''',
    '''.logo-img {
  height: 48px;
  width: 140px;'''
)

css = css.replace(
    '''.footer .logo-img {
  height: 52px;
  width: auto;''',
    '''.footer .logo-img {
  height: 52px;
  width: 150px;'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css")
