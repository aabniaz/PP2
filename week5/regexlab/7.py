import re
txt = open('text.txt', 'r', encoding='utf-8')
x = re.sub(r"([a-z]+)_", r"\1 ", txt.read())
x = re.split(" ", x)
s = ""
for i in x:
    s += "".join(i).capitalize()
print(s)