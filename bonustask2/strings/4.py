# Переставить два слова
s = str(input())
ab = s.find(' ')
print(s[ab + 1:], s[:ab])