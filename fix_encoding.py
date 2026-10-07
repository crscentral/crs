for f in ['chunk2.py', 'chunk3.py', 'chunk4.py']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    with open(f, 'w', encoding='utf-8') as file:
        file.write('# -*- coding: utf-8 -*-\n' + content)
