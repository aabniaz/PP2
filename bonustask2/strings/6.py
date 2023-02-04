# Второе вхождение
s = str(input())
f = s.count('f')
if f == 1:
    print(-1)
elif f < 1:
    print(-2)
else:
    a = s.find('f') + 1
    print(s.find('f', a))