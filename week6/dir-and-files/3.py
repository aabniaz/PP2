import os
path = "C:\Users\user\Desktop\PP2\week5\regexlab\text.txt"
if os.path.exists(path):
    fileName = os.path.basename(path)
    path_to_file = os.path.dirname(path)
    print(fileName)
    print(path_to_file)
else:
    print("The path does not exist")