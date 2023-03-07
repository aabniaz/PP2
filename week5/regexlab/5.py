import re
txt = open('text.txt', 'r', encoding='utf-8')
x = re.findall("^a.*b$", txt.read())
if x: print("YES", x)
else: print("NO")