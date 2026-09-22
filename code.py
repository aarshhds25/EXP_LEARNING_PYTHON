import math


def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  if y == 0:
    return "Error! Division by zero."
  return x / y


def power(x, y):
  return x**y


def square_root(x):
  if x < 0:
    return "Error! Cannot calculate square root of a negative number."
  return math.sqrt(x)


def calculator():
  print("=" * 40)
  print("         SIMPLE PYTHON CALCULATOR       ")
  print("=" * 40)

  while True:
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Exit")

    choice = input("\nEnter choice (1-9): ").strip()

    if choice == "9":
      print("\nThank you for using the calculator. Goodbye!")
      break

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
      print("Invalid choice! Please select a valid option (1-9).")
      continue

    try:
      # Operations requiring only ONE input
      if choice == "6":
        num = float(input("Enter number: "))
        result = square_root(num)
        print(f"Result: √{num} = {result}")

      elif choice == "7":
        degrees = float(input("Enter angle in degrees: "))
        radians = math.radians(degrees)
        print(f"Result: sin({degrees}°) = {math.sin(radians)}")

      elif choice == "8":
        degrees = float(input("Enter angle in degrees: "))
        radians = math.radians(degrees)
        print(f"Result: cos({degrees}°) = {math.cos(radians)}")

      # Operations requiring TWO inputs
      else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
          print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
          print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
          print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
          print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == "5":
          print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")

    except ValueError:
      print("Invalid input! Please enter numeric values only.")


# Run the calculator
if __name__ == "__main__":
  calculator()
