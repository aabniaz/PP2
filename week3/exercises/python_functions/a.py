#1
def my_function():
  print("Hello from a function")

#2 
def my_function():
  print("Hello from a function")

my_function()

#3 first parameter
def my_function(fname, lname):
  print(fname)

#4
def my_function(x):
    return x + 5

#5 If you do not know the number of arguments that will be passed into your function
def my_function(*kids):
  print("The youngest child is " + kids[2])

#6 If you do not know the number of keyword arguments that will be passed into your function:
def my_function(**kid):
  print("His last name is " + kid["lname"])
