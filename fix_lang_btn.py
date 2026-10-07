with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if ".lang-btn {" in line:
        lines.insert(i+1, "  white-space: nowrap;\n")
        break

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.writelines(lines)
