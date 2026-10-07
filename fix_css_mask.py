with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I reverted the commit, so style.css still has filter: brightness(0) invert(1)
css = css.replace(
    'filter: brightness(0) invert(1); /* White fonts logo on dark background */',
    '''filter: none !important;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center left;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center left;
  object-position: -99999px; /* Hides original black image data */
  color: transparent;'''
)

css = css.replace(
    'filter: brightness(0) invert(1); /* White fonts logo in dark footer */',
    '''filter: none !important;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center left;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center left;
  object-position: -99999px;
  color: transparent;'''
)

css = css.replace(
    'filter: brightness(0) invert(1); /* Forces logo color to solid white */',
    '''filter: none !important;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center left;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center left;
  object-position: -99999px;
  color: transparent;'''
)

# For hero-logo-img, we might need center
css = css.replace(
    '''  filter: none !important;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center left;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center left;
  object-position: -99999px; /* Hides original black image data */
  color: transparent;
}

.hero-title {''',
    '''  filter: none !important;
  background-color: #ffffff;
  -webkit-mask-image: url('../images/logo_globe_transparent.webp');
  -webkit-mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center;
  mask-image: url('../images/logo_globe_transparent.webp');
  mask-size: contain;
  mask-repeat: no-repeat;
  mask-position: center;
  object-position: -99999px;
  color: transparent;
}

.hero-title {'''
)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with object-position mask trick")
