#my_list = [i for i in range(1, 10)]
my_list = list(map(int, input().split()))
product = 1
for i in range(len(my_list)):
    product *= my_list[i]
print(product)

