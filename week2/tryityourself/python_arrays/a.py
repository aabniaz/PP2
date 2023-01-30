#1
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#2
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

#3 
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

#4 
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

#5 each item in the cars array
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

#6 add
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

#7 Delete the second element of the cars array
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

#8 Delete the element that has the value "Volvo"
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
