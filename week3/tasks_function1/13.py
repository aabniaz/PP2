import random
my_number = random.randint(1, 10)
print("Hello! What is your name?")
input_name = input()
text = "Well, {}, I am thinking of a number between 1 and 20."
print(text.format(input_name), "\nTake a guess.")
trying = 0
while(True):
    input_number = int(input())
    trying += 1
    if input_number == my_number:
        text = "\nGood job, {} You guessed my number in {} guesses!"
        print(text.format(input_name, trying))
        break
    else:
        print("\nYour guess is too low. \nTake a guess.")
input()

