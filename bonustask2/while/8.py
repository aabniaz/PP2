# Максимум последовательности
x = 0
n = int(input())
while n != 0:
    if n > x:
        x = n
    n = int(input())
print (x)
