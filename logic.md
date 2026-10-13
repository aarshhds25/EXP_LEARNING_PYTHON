==>Code Logic

1.Import math module:
    You bring in Python’s math library so you can use advanced functions like sin, cos, log, and sqrt.
    
2. History list created
    history = [] initializes an empty list.
    This list will store all past calculations as strings (like "5 + 3 = 8").
   
3.Infinite loop (while True)
    Keeps the calculator running until the user chooses to exit.
    Each loop shows a menu with four options.

4.User choice (if-elif-else)

Choice 1 → Basic Calculator
        Takes two numbers and an operator (+, -, *, /).
        Performs the calculation using if-elif.
        Stores the result in history using append().
        Uses try-except to handle invalid inputs (like letters instead of numbers).

Choice 2 → Advanced Operations
        Asks for one number and an advanced operation (sin, cos, log, sqrt).
        Uses math functions to calculate.
        Stores the result in history.
        Again uses try-except for error handling.

Choice 3 → Show History
        Loops through the history list and prints each stored calculation.

Choice 4 → Exit
        Breaks the loop and ends the program.
        Else → Invalid Choice
        If the user enters something other than 1–4, it shows an error message.

--------Key Concepts Used-------
    
List (history) → Stores past results.
1. .append() → Adds new results to the list.
2. f-string (f"{num1} {op} {num2} = {result}") → Formats variables into a readable string.
3. while True loop → Keeps the program running until exit.
4. if-elif-else → Decision making for operations.
5. try-except → Prevents program crash on invalid input.
6. math module → Provides advanced math functions.
