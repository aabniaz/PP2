# Количество четных элементов последовательности
n = int(input())
x = 0
while n != 0:
    if n % 2 == 0:
        x += 1
    n = int(input())    
print(x)
