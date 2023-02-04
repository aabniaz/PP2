# Две половинки
s = str(input())
print(s[(len(s)+1) // 2:] + s[:(len(s)+1) // 2])

"""
s = str(input())
sp = (len(s)+1)//2
b = s[sp:len(s)] + s[:sp]
print(b)

"""