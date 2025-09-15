# Q12. Create a number guessing game.
import random

number = random.randint(1,100)
guess = None

print("guess any number between 1 to 100")

while guess!= number:
    guess = int(input("Enter your guess:"))

    if guess > number:
        print("too large guess some smaller number")
    elif guess < number :
        print("too small guess some bigger number")

    else :
        print("hurray you guess it correct the number is :" ,number)