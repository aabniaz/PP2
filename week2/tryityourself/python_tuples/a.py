# Tuple items are ordered, unchangeable, and allow duplicate values
#1 tuple allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#2
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#3
"""To create a tuple with only one item, 
you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple."""
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple") #tuple
print(type(thistuple)) #str
 
#4 any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#5
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#6
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#7 Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


