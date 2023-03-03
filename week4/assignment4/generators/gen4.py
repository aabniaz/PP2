def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a = squares(1, 10)
for elem in a:
    print(elem)