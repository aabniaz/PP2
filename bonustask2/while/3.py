# Степень двойки
n = int(input())
p = 0
st = 1
while st <= n:
    p += 1
    st *= 2
print(p - 1,st // 2)
