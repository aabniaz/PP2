def squares(a,n):
    for i in range(a, n+1):
        yield i * i


a = squares(1,10)
for elem in a:
    print(elem)