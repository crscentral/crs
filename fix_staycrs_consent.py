import re
with open('staycrs.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    'return "StayCRS demo request\\n\\nName: "+g(\'n\')+"\\nCountry: "+g(\'c\')+"\\nHotel: "+g(\'h\')+"\\nEmail: "+g(\'e\')+"\\nPhone: "+g(\'p\')+"\\nRooms: "+g(\'r\')+"\\nInterested in: "+g(\'i\');',
    'var p=document.getElementById(\'privacyConsent\')?document.getElementById(\'privacyConsent\').checked:"No";\n  return "StayCRS demo request\\n\\nName: "+g(\'n\')+"\\nCountry: "+g(\'c\')+"\\nHotel: "+g(\'h\')+"\\nEmail: "+g(\'e\')+"\\nPhone: "+g(\'p\')+"\\nRooms: "+g(\'r\')+"\\nInterested in: "+g(\'i\')+"\\nPrivacy Consent: "+p;'
)

with open('staycrs.html', 'w', encoding='utf-8') as f:
    f.write(html)
