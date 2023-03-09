import os
path = r"C:\Users\user\Desktop\PP2\week5\regexlab\text.txt"
f = open(path)
if os.path.exists(path):
    print("YES, the path is exist!")
else:
    print("does not exist :(")

print(f.readable())
print(f.writable()) #доступен просмотр

if os.access(path, os.X_OK): #Checks if path can be executed
    print("YES, it's executable!")
else:
    print("NO")