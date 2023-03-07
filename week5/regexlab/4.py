import re
txt = open('text.txt', 'r', encoding='utf-8')
x = re.findall('[A-Z][a-z]+', txt.read())
print(x)