import re
#txt = open(r"C:\Users\user\Desktop\PP2\week5\regexlab\text.txt", "r", "utf-8")
txt = open('text.txt', 'r', encoding='utf-8')
result = re.findall(".*a.*b*", txt.read())
print(result)