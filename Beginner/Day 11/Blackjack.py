
import random
from art import logo
print(logo)

print("WELCOME TO A GAME OF BLACKJACK")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def lose_condition (sum_of_cards):
    if sum_of_cards > 21:
        print("You lose!")


def lose_condition_1 (sum_of_cards_1):
    if sum_of_cards_1 > 21:
        print("You Win!")

while True:     #EASY METHOD TO MAKE THE WHOLE LOOP REPEAT (BANGER)
    status = input("Do you want to play a game of BlackJack. Type y or n: ").lower()
    if status == "y":
        player_card = random.sample(cards, 2)
        sum_card = sum(player_card)
        print(f"Your cards: {player_card} , Current Score: {sum_card}")
        computer_card = []
        computer_card = random.sample(cards, 1)
        sum_card_1 = sum(computer_card)
        print(f"Computer's first card: {computer_card}")
        move_ahead = True
        while move_ahead:
            status_1 = input("Type y to hit for another card or press n to pass: ").lower()
            if status_1 == "y":
                new_card = random.choice(cards)
                player_card.append(new_card)
                sum_card += new_card
                print(f"Your cards: {player_card} , Current Score: {sum_card}")
                print(f"Computer's first card: {computer_card}")
                lose_condition(sum_card)

            else:
                move_ahead = False
                move_status = True
                while move_status:
                    if sum_card_1 < 17:
                        new_card1 = random.choice(cards)
                        computer_card.append(new_card1)
                        sum_card_1 += new_card1
                        lose_condition_1(sum_card_1)
                    else:
                        move_status = False
                print(f"Your final cards: {player_card} , Final Score: {sum_card}")
                print(f"Computer's final cards: {computer_card}, Final Score: {sum_card_1}")

        if sum_card <= 21 and sum_card_1 <= 21:
            a = 21 - sum_card
            b = 21 - sum_card_1
            if a < b:
                print("You win!")
            elif a > b:
                print("You lose!")
            elif a == b:
                print("Draw!")



