# Python Pattern Program

# Loop

# Outer Loop - Control rows
# Inner Loop - Control Column / numbers / stars
# range() - Control repetation
# end="" - Print on the same line
# print() - Moves to the next line
# if-else - Create special patterns

# Without-Space pattern

#1. Star Triangle
'''
print("\n STAR TRIANGLE")

rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(i):
        print("*" , end="  ")
    print()
'''
#2. Inverted star triangle
'''
print("\n Inverted star triangle")

rows = int(input("Enter number of rows:"))

for i in range(rows , 0 , -1):
    for j in range(i):
        print("*" , end="  ")
    print()
'''
#3. Number triangle
'''
rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(i):
        print(i , end=" ")
    print()

rows = int(input("Enter number of rows:"))

for i in range(rows , 0 , -1):
    for j in range(i):
        print(i , end=" ")
    print()
'''
# Continuoes Number Triangle

''''
rows = int(input("Enter number of rows:"))
number = 1

for i in range(1  , rows + 1):
    for j in range(i):
        print(number , end=" ")
        number += 1
    print()
'''

# With-Space Pattern

# right-angle triangle
'''
rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(rows - i):
        print("  "  ,end=" ")
    for j in range(i):
        print("*" , end=" ")
    print()
'''
rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(rows - i):
        print("  " , end=" ")
    for j in range(2 * i - 1):
        print("*" , end=" ")
    print()




        


