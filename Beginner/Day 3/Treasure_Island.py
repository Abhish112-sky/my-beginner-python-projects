print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
dir1 = input("Do you want to proceed Left or Right? ").lower()
if dir1 == "left":
    dir2 = input("Great Success. Do you want to Swim or Wait? ").lower()
    if dir2 == "wait":
        dir3 = input("Great Success. You come across 3 colored doors. Do you want to choose Red, Blue or Green door? ").lower()
        if dir3 == "red":
            print("Wrong choice. Burned by fire. Game over")
        elif dir3 == "blue":
            print("Wrong choice. Eaten by beasts. Game over")
        elif dir3 == "green":
            print("Great Success. You win the treasure")
        else:
            print("Wrong choice. Game over")
    else:
        print("Wrong choice. Attacked by Trout. Game over")
else:
    print("Wrong choice. Fall into a hole. Game over")


