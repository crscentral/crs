with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if ".dropdown-toggle {" in line:
        # insert white-space: nowrap; after it
        lines.insert(i+1, "  white-space: nowrap;\n")
        break

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.writelines(lines)
