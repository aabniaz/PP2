# Номер числа Фибоначчи
x = 0
x1 = 1
x2 = 0
i = 0
n = int(input())
while x <= n:
    x = x1 + x2
    x1, x2 = x, x1
    i += 1
if (n == x2):
    print(i)
else:
    print(-1)