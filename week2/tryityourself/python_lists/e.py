#1 Remove "banana"
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#2 The pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#3 If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#4 The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#5 Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

#6
"""
The clear() method empties the list.
The list still remains, but it has no content."""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

