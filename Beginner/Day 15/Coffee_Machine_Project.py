MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def coins():
    a = int(input("How many quarters would you like to enter?: "))
    b = int(input("How many dimes would you like to enter?: "))
    c = int(input("How many nickels would you like to enter?: "))
    d = int(input("How many pennies would you like to enter?: "))
    entered_amt = round((a*0.25 + b*0.1 + c*0.05 + d*0.01), 2)
    return entered_amt

def resource_check(drink_name, dict, dict1):
    enough_resources = True
    for key in dict:
        if dict[key] < dict1[drink_name]["ingredients"][key]:
            print(f"Sorry human, there is not enough {key} to make {drink_name}.")
            enough_resources = False
            break
    return enough_resources

def main_function(drink_name, dict, dict1):
    print(f"Start entering your coins for the {drink_name}.")
    entered_money = coins()
    if entered_money < dict1[drink_name]["cost"]:
        print("Sorry human, there is not enough money to make coffee. Money Refunded. ")

    else:
        change = round(entered_money - dict1[drink_name]["cost"], 2)
        print(f"Here is ${change} in change.")
        for key in dict:
            dict[key] = dict[key] - dict1[drink_name]["ingredients"][key]
        print("HERE IS YOUR COFFEE. CIAO HUMAN")


print("WELCOME TO THE COFFEE MACHINE, HUMAN!!")
move_ahead = True
profit = 0
while move_ahead:
    user_want = input("What would you like to have today? Type espresso, latte or cappuccino: ").lower()
    if user_want == "report":
        print(resources)
    elif user_want == "off":
        move_ahead = False
    elif resource_check(user_want, resources, MENU) == True:
        main_function(user_want, resources, MENU)
        profit += MENU[user_want]["cost"]
   







