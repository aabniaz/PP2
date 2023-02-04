# Количество элементов, равных максимуму1
element = int(input())
number = 1
max = 0
while element != 0:
    if element == max:
        number += 1
    elif element > max:
        max = element
        number = 1
    element = int(input())
print(number)
