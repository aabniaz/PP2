#1 second item
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#2 -1 last item
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi'], the item in position 5 is NOT included

#4 items from index 0 to index 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

#5 the items from index 2 to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#6 the items from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



