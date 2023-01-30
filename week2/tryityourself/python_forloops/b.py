#1 0 to 5, not including 6
for x in range(6):
  print(x)

#2 2,3,4,5
for x in range(2, 6):
  print(x)

#3 Increment the sequence with 3
for x in range(2, 30, 3):
  print(x)

#4
for x in range(6):
  print(x)
else: #The else block will NOT be executed if the loop is stopped by a break statement.
  print("Finally finished!")

#5
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.


#6 A nested loop is a loop inside a loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#7
for x in [0, 1, 2]:
  pass 
"""for loops cannot be empty, 
but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error."""


