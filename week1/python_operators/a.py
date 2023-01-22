#1 Addition
print(5 + 10) 
#2 Subtraction
print(15 - 10) 
#3	Multiplication
print(5 * 10) 
#4 Division
print(50 / 10) 
print(25 / 10) 
#5 Modulus
print(5 % 2) 
#6 Exponentiation
print(2 ** 5)
#7 Floor division; rounds the result down to the nearest whole number
print(15 // 2)
print("\n")
#8
"""
=	    x = 5	    x = 5           5   
+=	    x += 3	    x = x + 3       8
-=	    x -= 3	    x = x - 3	    2
*=	    x *= 3	    x = x * 3	    15
/=	    x /= 3	    x = x / 3	    1.6666666666666667
%=	    x %= 3	    x = x % 3	    2
**=	    x **= 3	    x = x ** 3	    125
"""
x = 5
x += 4
print(x) #9
print("\n")
#9
x = 5
y = 3
print(x == y) #false
print(x != y) #true
print(x > y)    #true
print(x < y)    #false
print(x >= y)   #true
print(x <= y)   #false
print("\n")
#10
x = 5   
print(x > 3 and x < 10) #true AND & True if both statements are true
x = 5
print(x > 3 or x < 4)   #true OR | True if one of the statements is true
x = 5
print(not(x > 3 and x < 10))    #false NOT ~ False if the result is true
print("\n")
#11
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True because z is the same object as x
print(x is y) #False because x is not the same object as y, even if they have the same content
print(x == y) #to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print("\n")
#12
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) #False because z is the same object as x
print(x is not y) #True because x is not the same object as y, even if they have the same content
print(x != y) #to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print("\n")
#13
x = ["banana", "apple"]
print("banana" in x) #true
print("cherry" not in x) #true
