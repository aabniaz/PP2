f = open("demofile2.txt", "x")
f.write("Now this file has a content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())