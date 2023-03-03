def generate(n):
    for i in range(n+1):
        if i%12==0:
            yield i

n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))