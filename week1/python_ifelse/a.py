#1
a = 33
b = 200
if b > a:
    print("b is greater than") #b is greater than a
#2
"""
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error"""
#3
a = 200 
b = 33
if b > a:
    print("b is greater than a")
elif a == b:   #elif -> if the previous conditions were not true, then try this condition
    print("a and b are equal")
else:
    print("a is greater than b") #a is greater than b
#3
a = 2
b = 300
print("A") if a > b else print("B") #B
#4
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #=
#5 and
a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are true")   #both conditions are true
#6 or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("at least one of the conditions are true")    #at least one of the conditions are true
#7 nested if
x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above ten")
    else:
        print("but not above 20")
"""Above ten
and also above ten"""
#8 
""" if statements cannot be empty, 
    but if you for some reason have an if statement with no content, 
    put in the pass statement to avoid getting an error."""
a = 33
b = 200
if a > b:
    pass



    

         