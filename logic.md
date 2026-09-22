[ START ]
    │
    ▼
1. Show Menu & Ask: "What do you want to do?" (Choose 1-9)
    │
    ├─► If 9: STOP the program.
    │
    ├─► If invalid option: Say "Invalid choice" ──► Go back to menu.
    │
    └─► If valid option (1-8):
            │
            ▼
        2. Ask user for number(s)
            │
            ├─► Did they type text instead of numbers? ──► Say "Numbers only!" ──► Go back to menu.
            │
            └─► Did they type valid numbers?
                    │
                    ▼
                3. Do the math (add, subtract, multiply, divide, etc.)
                    │
                    ├─► Trying to divide by zero? ──► Say "Error!"
                    └─► Valid math? ──► Print the Result
                            │
                            ▼
                4. Repeat process ──► Go back to menu.
