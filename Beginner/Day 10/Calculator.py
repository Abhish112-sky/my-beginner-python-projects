from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operator = {
    "Add" : "+",
    "Subtract" : "-",
    "Multiply" : "*",
    "Divide" : "/"
}

def operation(operator_input):
    if operator_input == "+":
        return add(input_1, input_2)
    elif operator_input == "-":
        return subtract(input_1, input_2)
    elif operator_input == "*":
        return multiply(input_1, input_2)
    elif operator_input == "/":
        return divide(input_1, input_2)
    else:
        print("Invalid operator")
        return

restart_status = True
while restart_status:
    input_1 = int(input("Enter the first number: "))
    for key in operator:
        print(operator[key])
    op_input = input("Pick an operator: ")
    input_2 = int(input("Enter the second number: "))
    results_initial = operation(op_input)

    print(f"{input_1} {op_input} {input_2} = {results_initial}")

    input_text = input(f"Type y to continue calculating with {results_initial} and type n to start a new calculation.\n")
    should_continue = True
    while should_continue:
        if input_text == "n":
            should_continue = False
        else:
            input_1 = results_initial
            for key in operator:
                print(operator[key])
            op_input_2 = input("Pick an operator: ")
            input_2 = int(input("Enter the second number: "))
            results_initial= operation(op_input_2)

            print(f"{input_1} {op_input_2} {input_2} = {results_initial}")

            input_text = input(f"Type y to continue calculating with {results_initial} and type n to start a new calculation.\n")




