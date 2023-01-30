#1
i = 1
while i < 6:
  print(i)
  i += 1

#2
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break #the break statement can stop the loop even if the while condition is true
  i += 1

#3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #the continue statement can stop the current iteration, and continue with the next
  print(i)

#4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")