# __ doc __

#print(greet.__doc__)

#print(student_details.__doc__)


# 1. Recursive function to calculate factorial number
'''
def factorial(n):

    if n < 0:
        return "Factorial is not possible for nagative number"
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


num = int(input("Enter a number:"))
print(factorial(num))
'''
# 2. Fibonacci sequence
'''
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a number:"))

print(fibonacci(num))
'''
# String Reverse using Recursive Function
'''
def rev_str(text):
    if len(text) == 0:
        return ""
    return rev_str(text[1:]) + text[0]

text = input("Enter a string:")

print(text)
print(rev_str(text))
'''
# Lambda Function
'''
square = lambda x : x * x

num = int(input("Enter a number:"))

print(square(num))


number = [1 , 2 , 3 , 4 , 5 , 6]

result = list(map(lambda x : x * x , number))

print(result)

filter_result = list(filter(lambda x : x % 2 == 0 , number))

print(filter_result)

'''
'''
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))

largest = lambda a , b , c : max(a , b , c)

smallest = lambda a , b , c : min(a , b , c)

print(largest(n1 , n2 , n3))

print(smallest(n1 , n2 , n3))
'''

# Global Variables
'''
total = 0

def add_number(num):
    global total
    total += num
  

n = int(input("How many number do you want to enter?"))

for i in range(n):
    num = int(input("Enter number :"))
    add_number(num)

print("Total Sum :" , total)
    

'''
'''
username = "Guest"

def change_username(new_name):
    global username
    username = new_name

print(username)

new_username = input("Enter new username:")

change_username(new_username)

print(username)
'''
value = 100

def show_value():
    value = 50
    print(value)

show_value()

print(value)

# Function task list and returns:

def list_operation(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total , maximum , minimum

numbers = [10 , 20 , 30 , 40 , 50]

total , maximum , minimum = list_operation(numbers)

print(total)
print(maximum)
print(minimum)

# 1D array

# A 1D array in python is represented using a list.

# Types of Arrays in Python

# 1. Homogeneous Array

# A Homogeneous array contains element of the same data type.

number = [10 , 20 , 30 , 40 , 50]

fruits= ['apple' , 'banana' , 'orange' , 'mango']

#2. Heterogeneous Array

# A Heterogenous array contain element of the diffrent data types.

student = ["vivek" , 25 , 89.60 , True]

print(student)


# Typecodes

'''
'i' integer array('i' , [10 , 20 , 30])
'f' float     array('f' , [10.2 , 20.5])
'd'double array('d' , [10 .25 , 20.65])
'u' unicode character  array('u' , 'python')
'''











