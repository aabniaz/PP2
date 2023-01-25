#1.
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))
print("\n")

#2. int
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
print("\n")

#3. float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
print("\n")

#4. Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print("\n")

#5. complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
print("\n")

#6. 
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))
print("\n")

#7. Random number
import random

print(random.randrange(1, 10))
