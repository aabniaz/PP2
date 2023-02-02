#Шахматная доска
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if ((x + y) % 2)  == ((x1 + y1) % 2):
    print("YES")
else:
    print("NO")
