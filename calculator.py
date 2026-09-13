# Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Take two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Ask the user for an arithmetic operation
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
        print("Result:", result)

    elif operation == "-":
        result = num1 - num2
        print("Result:", result)

    elif operation == "*":
        result = num1 * num2
        print("Result:", result)

    elif operation == "/":
        # Prevent division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        # Handle an invalid operation
        print("Error: Invalid operation.")

except ValueError:
    # Handle invalid number input
    print("Error: Please enter valid numbers.")
