letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
password = ""
for i in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
for i in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols
for i in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers
print(password)

new_password = random.shuffle(password)
random_password = ""
for n1 in new_password:
    random_password = random_password + n1
print(random_password)
