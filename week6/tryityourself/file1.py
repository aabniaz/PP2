f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(14))

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()