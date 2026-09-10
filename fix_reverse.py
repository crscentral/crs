import re

with open('laos.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="split-layout reverse">', '<div class="split-layout">')

# Then find "What We Do in Vientiane Section" and add reverse to it
idx1 = content.find('<!-- What We Do in Vientiane Section -->')
if idx1 != -1:
    section1 = content[idx1:idx1+1000]
    section1_new = section1.replace('<div class="split-layout">', '<div class="split-layout reverse">', 1)
    content = content.replace(section1, section1_new)

# And add reverse to "Laos Advantage Section"
idx2 = content.find('<!-- Laos Advantage Section -->')
if idx2 != -1:
    section2 = content[idx2:idx2+1000]
    section2_new = section2.replace('<div class="split-layout">', '<div class="split-layout reverse">', 1)
    content = content.replace(section2, section2_new)

with open('laos.html', 'w', encoding='utf-8') as f:
    f.write(content)

