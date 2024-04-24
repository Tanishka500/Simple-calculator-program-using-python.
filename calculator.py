def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")

    operation_choice = input("Enter choice (1/2/3/4/5/6/7): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation_choice == '1':
        result = num1 + num2
    elif operation_choice == '2':
        result = num1 - num2
    elif operation_choice == '3':
        result = num1 * num2
    elif operation_choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        else:
            result = num1 / num2
    elif operation_choice == '5':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        else:
            result = num1 // num2
    elif operation_choice == '6':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        else:
            result = num1 % num2
    elif operation_choice == '7':
        result = num1 ** num2
    else:
        print("Invalid Input")
        return

    print("Result:", result)

calculator()