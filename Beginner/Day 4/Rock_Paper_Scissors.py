rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the Rock Paper Scissors game!")
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choice = [rock, paper, scissors]
import random
random_choice = random.choice(choice)

if user_input > 2 or user_input < 0:
    print("You chose an invalid option.")
if user_input == 0:
    print(rock)
    print("The computer chose: ", random_choice)
    if random_choice == choice[1]:
        print("You lose!")
    elif random_choice == choice[0]:
        print("Its a draw!")
    else:
        print("You win!")
if user_input == 1:
    print(paper)
    print("The computer chose: ", random_choice)
    if random_choice == choice[2]:
        print("You lose!")
    elif random_choice == choice[1]:
        print("Its a draw!")
    else:
        print("You win!")
if user_input == 2:
    print(scissors)
    print("The computer chose: ", random_choice)
    if random_choice == choice[0]:
        print("You lose!")
    elif random_choice == choice[2]:
        print("Its a draw!")
    else:
        print("You win!")
