def calculator():
    # Prompt the user to enter the first number
    value1 = float(input("Enter the first value: "))

    # Prompt the user to enter the second number
    value2 = float(input("Enter the second value: "))

    # Display operation choices
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to choose an operation
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the chosen operation
    if operation == '1':
        result = value1 + value2
        operation_sign = '+'
    elif operation == '2':
        result = value1 - value2
        operation_sign = '-'
    elif operation == '3':
        result = value1 * value2
        operation_sign = '*'
    elif operation == '4':
        if value2 != 0:
            result = value1 / value2
            operation_sign = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"The result of {value1} {operation_sign} {value2} is: {result}")

# Run the calculator
calculator()
