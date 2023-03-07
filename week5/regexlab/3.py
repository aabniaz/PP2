import re 
txt = open('text.txt', 'r', encoding='utf-8')
result = re.findall('[a-z]+_[a-z]+', txt.read())
if result: print(result)
else: print("there is no snake_case in the text")