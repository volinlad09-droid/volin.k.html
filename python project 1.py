print("=" * 50)
print("      WELCOME TO PERSONAL DATA COLLECTOR")
print("=" * 50)

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
fav_num = int(input("Enter your favourite number: "))

# Calculation
birth_year = 2026 - age

# Displaying collected information
print("\n" + "=" * 50)
print("        INFORMATION COLLECTED")
print("=" * 50)

print("\nName:", name)
print("Data Type:", type(name))
print("Memory Address:", id(name))

print("\nAge:", age)
print("Data Type:", type(age))
print("Memory Address:", id(age))

print("\nHeight:", height)
print("Data Type:", type(height))
print("Memory Address:", id(height))

print("\nFavourite Number:", fav_num)
print("Data Type:", type(fav_num))
print("Memory Address:", id(fav_num))

# Type Casting Example
fav_num_float = float(fav_num)

print("\n" + "=" * 50)
print("CALCULATIONS")
print("=" * 50)

print("Approximate Birth Year:", birth_year)
print("Favourite Number as Float:", fav_num_float)

print("\nThank you for using Personal Data Collector!")
print("Goodbye!")