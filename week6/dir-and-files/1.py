import os
root = r"C:\Users\user\Desktop\PP2"
directory = open("directory.txt", "x")
directory.write("list of only directories:\n")

for path, dirs, files in os.walk(root):
    for name in dirs:
        directory.write(name + "\n")
directory.close()

file = open("files.txt", "x")
file.write("list of only files:\n")
for path, dirs, files in os.walk(root):
    for name in files:
        file.write(name + "\n")
file.close()

all = open("all.txt", "x", encoding = "utf-8")
all.write("list of all directories and files:\n")
for path, dirs, files in os.walk(root):
    for name in files:
        all.write(os.path.join(path, name) + "\n")
all.close()
