# Среднее значение последовательности
a = int(input())
b = 0
c = 0
while a != 0:
    b += a
    a = int(input())
    c += 1
print(b / c)
