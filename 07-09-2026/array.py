
numbers = [10 , 20 , 30 , 40 , 50]

# Indexed Array

# Index start in array : 0
# Length calculate : 1
'''
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

for i in numbers:
    print(i)
'''
# Using for Loop + append()

# Ask the user how many element they want to enter.
# create an empty list
# use a for loop to take input
# Store each element using append().
'''
size  = int(input("Enter size of Array : "))

numbers = [10 , 20 , 30 , 40 , 50]

for i in range(size):
    value = int(input(f"Enter Element {i + 1} :"))
    numbers.append(value)

print("\n Array Elements:")

print(numbers)

for i in numbers:
    print(i)
'''
# Using map() + split()


# Ask the user to enter all element in one line seperated by space.
# split() convert the input string into a list of string.
# map() convert each string into an integer.
# list() stores the result as a list.

'''
numbers = list(map(int , input("Enter array Elements:").split()))

for i in numbers:
    print(i)

print(numbers)
'''
#Using List Comprehension
'''
size  = int(input("Enter size of Array : "))

numbers = [int(input(f"Enter Element {i + 1}:")) for i in range(size)]

print(numbers)
'''




