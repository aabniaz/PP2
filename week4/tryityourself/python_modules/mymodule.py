#1
import mymodule

mymodule.greeting("Jonathan")

#2
import mymodule

a = mymodule.person1["age"]
print(a)

#3
import mymodule as mx

a = mx.person1["age"]
print(a)

#4
import platform

x = platform.system()
print(x)

#5
import platform

x = dir(platform)
print(x)

#6
from mymodule import person1

print (person1["age"])

