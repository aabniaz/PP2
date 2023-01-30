#1
fruits = ("apple", "banana", "cherry")
print(fruits)

#2 Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.

#3 Asterisk, If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#4 Add a list of values the "tropic" variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

