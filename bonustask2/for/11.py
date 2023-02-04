# Потерянная карточка
n = int(input())
sum_with_lost_n = n
sum_without_lost_n = 0
for i in range(1, n):
    sum_with_lost_n += i
    sum_without_lost_n += int(input())
print(sum_with_lost_n - sum_without_lost_n)
