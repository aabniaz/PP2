import re
txt = open('text.txt', 'r', encoding='utf-8')
x = re.sub('[ ,.]', ':', txt.read())
print("before", txt)
print("after", x)