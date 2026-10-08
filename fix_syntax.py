files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

import re

correct_css = """/* Final StayCRS Fixes - Aligned Version */
.logo { direction: ltr; flex-shrink: 0 !important; }
header .nav > a { flex-shrink: 0; margin-inline-end: auto; }
header .nav { gap: 2rem; }

/* Ensure items fit within the 1120px wrap without squishing the logo */
.links { gap: 16px !important; flex-shrink: 1; }
.links a { font-size: 0.9rem !important; }

@media (max-width: 1200px) {
  .links { gap: 10px !important; }
  .links a { font-size: 0.8rem !important; }
  .links .btn { padding: 6px 12px !important; }
}

@media (max-width: 900px) {
  .links { gap: 8px !important; }
  .links a { font-size: 0.75rem !important; }
  .links .btn { padding: 6px 10px !important; font-size: 0.75rem !important; }
  .lang-btn { font-size: 0.75rem !important; padding: 4px 6px !important; }
}

@media (max-width: 620px) {
  .nav.wrap { padding: 0 10px !important; gap: 10px !important; }
  .logo { height: 32px !important; }
  .links { gap: 8px !important; }
  .links .btn { padding: 6px 10px !important; font-size: 0.8rem !important; }
  .lang-btn { font-size: 0.8rem !important; padding: 4px 6px !important; }
}

/* Mobile Hamburger Nav for StayCRS */
@media (max-width: 900px) {
  .menu-toggle-btn { display: block !important; }
  header .wrap.nav { justify-content: space-between; position: relative; }
  .links {
    position: absolute;
    top: 68px;
    left: 0;
    right: 0;
    background: #fff;
    flex-direction: column;
    align-items: stretch !important;
    padding: 20px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    display: none !important;
    z-index: 1000;
  }
  .links.mobile-open {
    display: flex !important;
  }
  .links a:not(.btn) {
    display: block !important;
    padding: 12px 0 !important;
    border-bottom: 1px solid #eee;
    font-size: 1.1rem !important;
  }
  .links .btn {
    margin-top: 15px;
    text-align: center;
    width: 100%;
  }
  .lang-selector {
    margin-top: 15px;
    width: 100%;
  }
  .lang-btn {
    width: 100%;
    font-size: 1.1rem !important;
  }
}"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'/\* Final StayCRS Fixes - Aligned Version \*/.*?(?=</style>)', correct_css + '\n', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Restored perfect syntax")
