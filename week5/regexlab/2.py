import re 
txt = open('text.txt', 'r', encoding='utf-8')
result = re.findall(".*a.*b.*b.*b?.*", txt.read())
print(result)
