operand1 = None
operator = None
operand2 = None

def main():
    ask_user_input()
    # Perform the operation based on the operator
    match operator:
        case '+':
            result = operand1 + operand2
        case '-':
            result = operand1 - operand2
        case '*':
            result = operand1 * operand2
        case '/':
            if operand2 == 0:
                print("Error: Division by zero is undefined.")
                return
            result = operand1 / operand2
        case _:
            print("Invalid operator.")
            return

    # Print the result
    print("Result:", result)

def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = float(input("Enter the first operand: "));

    # Get the operator from the user
    global operator
    operator = input("Enter an operator (+, -, *, /): ");

    # Get second operand from the user
    global operand2
    operand2 = float(input("Enter the second operand: "));


# Call the main function to run the program
main()