import re
txt = open('text.txt', 'r', encoding='utf-8')
x = re.sub(r"([A-Z]|[a-z][a-z]*)([A-Z][a-z]*)", r"\1 \2 ", txt.read()).strip()
x = re.sub(" ", "_", x).lower()
print(x)