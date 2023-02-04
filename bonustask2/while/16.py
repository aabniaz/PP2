# Максимальное число идущих подряд равных элементов1
x = int(input())
n = 1
max = 1
while x != 0:
    a = x
    x = int(input())
    if x == a: 
        n += 1
        if n > max: max=n
    else: n = 1
print(max)
