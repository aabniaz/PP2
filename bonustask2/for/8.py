# Сумма факториалов
n = int(input())
product = 1
sum = 0
for i in range(1, n+1):
    product *= i
    sum += product
print(sum)
