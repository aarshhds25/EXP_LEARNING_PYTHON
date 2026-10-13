import math   # for Module‑2 (sin, cos, log, sqrt)

# MODULE 04: History list
history = []   # List to store past calculations

while True:   # Loop for multiple operations
    print("\n--- Calculator Menu ---")
    print("1. Basic Calculator (+, -, *, /)")
    print("2. Advanced Operations (sin, cos, log, sqrt)")
    print("3. Show History")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # MODULE 01: Basic Calculator
    if choice == "1":
        try:
            # Taking two numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Choose operation (+, -, *, /): ")

            # if-else for operation
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                print("Invalid Operator")
                continue

            print("Result =", result)
            history.append(f"{num1} {op} {num2} = {result}")  # Save in history

        except Exception:
            # MODULE 03: Error Handling
            print("Invalid Input! Please try again.")

    # MODULE 02: Advanced Operations
    elif choice == "2":
        try:
            print("Available: sin, cos, log, sqrt")
            op = input("Enter operation: ")

            num = float(input("Enter number: "))

            if op == "sin":
                result = math.sin(num)
            elif op == "cos":
                result = math.cos(num)
            elif op == "log":
                result = math.log(num)
            elif op == "sqrt":
                result = math.sqrt(num)
            else:
                print("Invalid Operator")
                continue

            print("Result =", result)
            history.append(f"{op}({num}) = {result}")  # Save in history which is a list

        except Exception:
            print("Invalid Input! Please try again.")

    # MODULE 04: Show History
    elif choice == "3":
        print("\n--- Calculation History ---")
        for item in history:
            print(item)

    # Exit option
    elif choice == "4":
        print("Exiting Calculator... Goodbye!")
        break

    else:
        print("Invalid Choice! Please enter 1-4.")
