from os import name

from art import logo
from art import vs
print(logo)
from game_data import data
import random
print("WELCOME TO THE GAME OF HIGHER OR LOWER")

comp = random.sample(data, 2)
game_over = False
score = 0
while not game_over:
    print(f"Compare A: {comp[0]["name"]}, a {comp[0]["description"]}, from {comp[0]["country"]}")
    print(vs)
    print(f"Against B: {comp[1]["name"]}, a {comp[1]["description"]}, from {comp[1]["country"]}")
    guess = input("WHO HAS MORE FOLLOWERS? TYPE A OR B: ").upper()
    if comp[0]["follower_count"] > comp[1]["follower_count"]:
        if guess == "A":
            score += 1
            print(f"THAT'S CORRECT. Your current score is: {score}")
        else:
            print("\n" * 20)
            print(logo)
            print(f"Sorry that's wrong. Your final score is: {score}")
            game_over = True
    elif comp[1]["follower_count"] > comp[0]["follower_count"]:
        if guess == "A":
            print("\n" * 20)
            print(logo)
            print(f"Sorry that's wrong. Your final score is: {score}")
            game_over = True
        else:
            score += 1
            print(f"THAT'S CORRECT. Your current score is: {score}")
    del comp[0]
    comp.append(random.choice(data))


