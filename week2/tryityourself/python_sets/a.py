# A set is a collection which is unordered, unchangeable*, and unindexed, and do not allow duplicate values.


#1 
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2 Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#3 
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#4 can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
 
#5 can contain different data types
set1 = {"abc", 34, True, 40, "male"}
print(set1)

#6 
myset = {"apple", "banana", "cherry"}
print(type(myset))

#7 It is also possible to use the set() constructor to make a set
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.