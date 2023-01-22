#1. The indentation in Python is very important:
if 5 > 2:
    print("Five is greater than two!")

#2. Python will give you an error if you skip the indentation:
"""
if 5 > 2:
print("Five is greater than two!")
"""

#3. Number of space: 4 or at least one:
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#4. Same number of spaces in the same block of code, otherwise Python will give an error:
"""
if 5 > 2:
 print("Five is greater than two!")  
        print("Five is greater than two!")
"""