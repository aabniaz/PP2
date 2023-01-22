#1. Global variables:
x = "awesome"

def myfunc():
  print("Python is " + x)
  print("\n")
myfunc()

#2.  
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print("\n")

#3. 
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print("\n")
#4.  
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

