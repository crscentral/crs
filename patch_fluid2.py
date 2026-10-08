import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Protect the logo globally by appending to the end of the file
css += "\n\n/* Global logo protection */\n.header-container > .logo-link {\n  flex-shrink: 0 !important;\n}\n"

# 2. Make fonts fluid on desktop
css = re.sub(r'\.nav-link\s*\{[^}]*font-size:\s*1\.0rem;', lambda m: m.group(0).replace('1.0rem', 'clamp(0.85rem, 1.25vw, 1.0rem)'), css)
css = re.sub(r'\.dropdown-toggle\s*\{[^}]*font-size:\s*1\.0rem;', lambda m: m.group(0).replace('1.0rem', 'clamp(0.85rem, 1.25vw, 1.0rem)'), css)
css = re.sub(r'\.lang-btn\s*\{[^}]*font-size:\s*1\.0rem;', lambda m: m.group(0).replace('1.0rem', 'clamp(0.85rem, 1.25vw, 1.0rem)'), css)

# 3. Completely replace the intermediate breakpoint to remove the hardcoded 1.2rem
bad_media = """/* Intermediate Viewports: Compress spacing to prevent nav wrapping */
@media (min-width: 1001px) and (max-width: 1200px) {
  .header-container {
    padding: 0 1rem;
  }
  
  .nav-menu {
    gap: 1.25rem;
  }
  
  .nav-link, .dropdown-toggle {
    font-size:  1.2rem;
  }
  
  .logo-link {
    padding: 5px 12px;
  }
  
  .logo-img {
    height: 38px;
  }
  
  .lang-btn {
  font-size: 0.85rem;
    padding: 0.4rem 0.8rem;
    font-size: 0.95rem;
  }
}"""

good_media = """/* Intermediate Viewports: Compress spacing to prevent nav wrapping */
@media (min-width: 1001px) and (max-width: 1200px) {
  .header-container {
    padding: 0 10px;
  }
  
  .nav-menu {
    gap: 0;
  }
  
  .logo-link {
    padding: 5px;
  }
  
  .logo-img {
    height: 36px;
  }
  
  .lang-btn {
    padding: 0.4rem 0.6rem;
  }
}"""

css = css.replace(bad_media, good_media)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied fluid typography correctly.")
