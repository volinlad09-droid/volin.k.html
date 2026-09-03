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

count = 0

def my_func():

    global count

    count += 1

    print("Function called")
    print(count)

my_func()
my_func()
my_func()












