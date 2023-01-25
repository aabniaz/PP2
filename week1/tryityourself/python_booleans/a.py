#1
print(10 > 9)   #true
print(10 < 9)   #false
print(10 == 9)  #false
#2
a = 200
b = 33
if b > a:
    print("b is greater than a\n")
else:
    print("b is not greater than a\n")  
#3
x = "hello"
y = 15
print(bool(x))  #true
print(bool(y))  #true
print("\n")
#4
print(bool("abc"))  #true
print(bool(123))    #true
print(bool(["banana", "apple", "cherry"]))  #true

"""
TRUE -> Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones. """
#5
print("\n")
print(bool(False))  #false
print(bool(0))  #false
print(bool(None))   #false
print(bool("")) #false
print(bool())   #false
print(bool([]))  #false
print(bool({})) #false

"""
FALSE -> empty values, such as (), [], {}, "", the number 0, and the value None"""
print("\n")
#6
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  #false
print("\n")
#7
def myFunction():
    return True
print(myFunction()) #true
print("\n")
#8
def myfunction():
    return True
if myfunction():
    print("yes")    #yes
else: print("no")
print("\n")
#9 Check if an object is an integer or not:
x = 200
print(isinstance(x, int))   #true
"""
Python also has many built-in functions that return a boolean value, 
like the isinstance() function, which can be used to determine 
if an object is of a certain data type:"""

