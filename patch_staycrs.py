import os
import re

files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

whatsapp_css = """
/* WhatsApp Float CSS */
.whatsapp-float {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 60px;
  height: 60px;
  background-color: #25d366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  z-index: 9999;
  border: 2px solid #ffffff;
}
.whatsapp-icon {
  width: 34px;
  height: 34px;
}
.whatsapp-float:hover {
  transform: translateY(-5px) scale(1.05);
  background-color: #20ba5a;
}
.whatsapp-badge {
  position: absolute;
  right: 75px;
  background-color: #ffffff;
  color: #128c7e;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 700;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(37, 211, 102, 0.3);
  white-space: nowrap;
}
.whatsapp-badge::after {
  content: "";
  position: absolute;
  right: -6px;
  top: 50%;
  transform: translateY(-50%);
  border-width: 6px 0 6px 6px;
  border-style: solid;
  border-color: transparent transparent transparent #ffffff;
  display: block;
  width: 0;
}
@media (max-width: 480px) {
  .whatsapp-float { bottom: 20px; right: 20px; width: 55px; height: 55px; }
  .whatsapp-icon { width: 30px; height: 30px; }
  .whatsapp-badge { display: none; }
}

/* Nav Fixes */
.links a, .lang-btn, .lang-option {
  white-space: nowrap !important;
}
@media (max-width: 1300px) {
  .links { gap: 12px !important; }
  .links a { font-size: 0.8rem !important; }
  .lang-btn { font-size: 0.8rem !important; padding: 4px 8px !important; }
}
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove margin-left: auto from lang-selector
    html = html.replace('margin-left: auto;', '')
    
    # 2. Add WhatsApp and Nav CSS right before </style>
    if '/* WhatsApp Float CSS */' not in html:
        html = html.replace('</style>', whatsapp_css + '\n</style>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Patched all 5 StayCRS files.")
