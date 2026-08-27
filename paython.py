# ============================================================
# PR.1 - FUNDAMENTAL BOOSTER
# Project: Interactive Personal Data Collector
# ============================================================

print("=" * 60)
print("Welcome to the Interactive Personal Data Collector!")
print("=" * 60)

print("\nThis program collects your personal information,")
print("performs some calculations, and displays data types")
print("and memory addresses using type() and id().")

# ------------------------------------------------------------
# 1. COLLECT INFORMATION
# ------------------------------------------------------------

print("\n----- Please Enter Your Information -----")

# Name - String
name = input("Please enter your name: ")

# Age - String converted to Integer
age = int(input("Please enter your age: "))

# Height - String converted to Float
height = float(input("Please enter your height in meters: "))

# Favourite number - String converted to Integer
favourite_number = int(input("Please enter your favourite number: "))


# ------------------------------------------------------------
# 2. DATA PROCESSING
# ------------------------------------------------------------

# The example in the project brief uses 2023
current_year = 2023

# Calculate approximate birth year
birth_year = current_year - age

# Arithmetic operators
age_plus_favourite = age + favourite_number
age_minus_favourite = age - favourite_number
age_times_favourite = age * favourite_number

# Avoid division by zero
if favourite_number != 0:
    age_divided_by_favourite = age / favourite_number
else:
    age_divided_by_favourite = "Cannot divide by zero"

# Convert height from meters to centimeters
height_in_cm = height * 100

# Convert float result to integer
height_rounded_cm = int(height_in_cm)


# ------------------------------------------------------------
# 3. DISPLAY INFORMATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("Thank You! Here is the information we collected:")
print("=" * 60)

print("\nName:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Favourite Number:", favourite_number)

# ------------------------------------------------------------
# 4. DISPLAY DATA TYPE AND MEMORY ADDRESS
# ------------------------------------------------------------

print("\n----- Variable Details -----")

print("\nName:")
print("Value:", name)
print("Data Type:", type(name))
print("Memory Address:", id(name))

print("\nAge:")
print("Value:", age)
print("Data Type:", type(age))
print("Memory Address:", id(age))

print("\nHeight:")
print("Value:", height)
print("Data Type:", type(height))
print("Memory Address:", id(height))

print("\nFavourite Number:")
print("Value:", favourite_number)
print("Data Type:", type(favourite_number))
print("Memory Address:", id(favourite_number))


# ------------------------------------------------------------
# 5. TYPE CASTING DEMONSTRATION
# ------------------------------------------------------------

print("\n----- Type Casting Demonstration -----")

print("Original height:", height, "meters")
print("Height converted to centimeters:", height_in_cm, "cm")
print("Height converted from float to integer:", height_rounded_cm, "cm")

print("\nType of height:", type(height))
print("Type of rounded height:", type(height_rounded_cm))


# ------------------------------------------------------------
# 6. ARITHMETIC OPERATORS
# ------------------------------------------------------------

print("\n----- Arithmetic Operations -----")

print("Age + Favourite Number =", age_plus_favourite)
print("Age - Favourite Number =", age_minus_favourite)
print("Age * Favourite Number =", age_times_favourite)
print("Age / Favourite Number =", age_divided_by_favourite)


# ------------------------------------------------------------
# 7. BIRTH YEAR
# ------------------------------------------------------------

print("\n----- Data Processing Result -----")

print(
    "Your approximate birth year is:",
    birth_year,
    "(based on your age of",
    age,
    ")"
)


# ------------------------------------------------------------
# 8. FINAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PERSONAL INFORMATION SUMMARY")
print("=" * 60)

print("Name              :", name)
print("Age               :", age)
print("Height            :", height, "meters")
print("Height in cm      :", height_rounded_cm, "cm")
print("Favourite Number  :", favourite_number)
print("Approx. Birth Year:", birth_year)

print("\nThank you for using the Personal Data Collector!")
print("Keep learning Python and explore more programming concepts.")
print("=" * 60)