#1 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #If the item to remove does not exist, remove() will raise an error.
print(thisset)

#2 
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)

#3 You can also use the pop() method to remove an item, 
# but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print(x) 
print(thisset)

#4 The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#5 The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

