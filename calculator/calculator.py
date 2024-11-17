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


calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(calculator_operations)
# for user first input
def calculator():
    first_number = float(input("What's the first number? "))
    continue_calculating = True

    while continue_calculating:
        # users choice of operation
        for operator in calculator_operations:
            print(operator)

        choose_operations = input("Choose an operation: ")

        second_number = float(input("What's the second number? "))

        answer = calculator_operations[choose_operations](first_number, second_number)
        
        print(f"{first_number} {choose_operations} {second_number} = {answer}")

        choose_to_continue = input(
            f"Type y to continue with the current {answer}, or n to start a new calculation: "
        )

        if choose_to_continue == "y":
            first_number = answer
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()

            # print(answer)

calculator()
