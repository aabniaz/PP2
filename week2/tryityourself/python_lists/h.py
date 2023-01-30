#1 List objects have a sort() method that will sort the list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
#thislist.sort(reverse = True)
print(thislist)

#2 Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
#thislist.sort(reverse = True)
print(thislist)

#3 Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#4 By default the sort() method is case sensitive, 
# resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#5 if you want a case-insensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#6 Reverse the order of the list items
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
