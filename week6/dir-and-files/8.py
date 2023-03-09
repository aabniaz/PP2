import os
path_dir = r'C:\Users\user\Desktop\PP2\week6\dir-and-files\for_remove.txt'
if os.path.exists(path_dir):
    print("Yes")
    os.remove(path_dir)
else:
    print("No")
    