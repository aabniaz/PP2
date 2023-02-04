# Утренняя пробежка
x=int(input())
y=int(input())
i=1
while x<y:
    x=x+x/10 # x *= 1.1
    i+=1
print(i)