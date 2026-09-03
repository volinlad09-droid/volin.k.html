# Python Built-in Functions Assignment
import random

# Q2: Negative float number operations
num = float(input("Enter a negative float number: "))
print("\nQ2 Results")
print("Absolute value:", abs(num))
print("Cube:", pow(num, 3))
print("Rounded to 2 decimal places:", round(num, 2))

# Q3: List of 5 random integers
numbers = [random.randint(1, 100) for _ in range(5)]
print("\nQ3 Results")
print("Random list:", numbers)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))
print("Type:", type(numbers))

# Q4: User-entered list operations
user_numbers = list(map(float, input("\nEnter numbers separated by spaces: ").split()))
print("\nQ4 Results")
print("Ascending order:", sorted(user_numbers))
print("Descending order:", sorted(user_numbers, reverse=True))
print("Reversed order:", list(reversed(user_numbers)))

# Extra examples: zip() and enumerate()
print("\nzip() example:")
names = ["A", "B", "C"]
marks = [80, 90, 85]
print(list(zip(names, marks)))

print("\nenumerate() example:")
for index, value in enumerate(numbers):
    print(index, value)
