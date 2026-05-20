# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


user_log = {}
should_continue = True
while should_continue is True:
    user_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid amount?: "))
    user_log[user_name] = bid_amount
    status_update = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if status_update == "yes":
        print("\n" *100)
    else:
        should_continue = False
        winner = ""
        max_bid = 0
        for key in user_log:
            if user_log[key] > max_bid:
                max_bid = user_log[key]
                winner = key
        print(f"The winner is {winner} with a maximum bid of ${max_bid}. ")
        print("Thank you for using this program")


        ########OR###########################################

def maximum_bidder(bidding_dictionary):
    winner = ""
    max_bid = 0
    for key in bidding_dictionary:
        bid_amount = bidding_dictionary[key]
        if bid_amount > max_bid:   #WE CAN REMOVE UPPER LINE AS WRITE IF AS bidding_dictionary[key] > max_bid also
            max_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a maximum bid of ${max_bid}. ")
    print("Thank you for using this program")

user_log = {}
should_continue = True
while should_continue is True:
    user_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid amount?: "))
    user_log[user_name] = bid_amount
    status_update = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if status_update == "yes":
        print("\n" *100)
    else:
        should_continue = False
        maximum_bidder(user_log)