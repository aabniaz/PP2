#1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#List items are ordered, changeable, and allow duplicate values

#2 Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3 length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4 List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#5 A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #<class 'list'>

#7 Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


