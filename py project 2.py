# Project: Logic Box (Pattern Generator & Number Analyzer)

while True:
    # 1. Menu Display
    print("\nWelcome to the Pattern Generator and Number Analyzer!")
    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Option 1: Right-angled Triangle (Left Aligned)
    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    # Option 2: Pyramid
    elif choice == 2:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            # Spaces ke liye
            for s in range(rows - i):
                print(" ", end="")
            # Stars ke liye
            for k in range(2 * i - 1):
                print("*", end="")
            print()

    # Option 3: Left-angled Triangle (Right Aligned)
    elif choice == 3:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            # Spaces ke liye
            for s in range(rows - i):
                print(" ", end="")
            # Stars ke liye
            for k in range(i):
                print("*", end="")
            print()

    # Option 4: Number Analyzer
    elif choice == 4:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total_sum = 0
        for num in range(start, end + 1):
            total_sum = total_sum + num
            
            # Odd / Even check
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

    # Option 5: Exit Program
    elif choice == 5:
        print("Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid choice, please select between 1 to 5.")

    print("-" * 50)
