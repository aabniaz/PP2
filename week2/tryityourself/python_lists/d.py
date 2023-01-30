#1 To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#2 Insert an item as the second position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#3 To append elements from another list to the current list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #The elements will be added to the end of the list.

#4 Add elements of a tuple to a list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

