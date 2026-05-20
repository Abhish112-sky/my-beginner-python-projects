import random
from art import logo
print(logo)

print("Welcome to Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")
my_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type easy or hard: ").lower()

def guess_number(diff, attempts):
    move_ahead = True
    while attempts > 0 and move_ahead == True:
        print(f"You have {attempts} attempts to guess the number. ")
        guess = int(input("Make a guess: "))
        if guess > my_number:
            print("Too high!")
            print("Guess again.")
        elif guess < my_number:
            print("Too low!")
            print("Guess again.")
        else:
            print(f"You guessed my number! My number was {guess}.")
            print(f"You guessed the correct number in {(10 - attempts) + 1} attempts.")
            move_ahead = False
        attempts -= 1
    if attempts == 0:
        print("You ran out of attempts! GAME OVER!")
        move_ahead = False


if difficulty == "easy":
    attempts = 10
    guess_number(difficulty, attempts)
elif difficulty == "hard":
    attempts = 5
    guess_number(difficulty, attempts)
else:
    print("Invalid input. Try again later.")
