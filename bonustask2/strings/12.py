# Удалить каждый третий символ
s = str(input())
for i in range(0,len(s)):
    if i % 3 == 0:
        continue
    else:
        print(s[i],end = '')