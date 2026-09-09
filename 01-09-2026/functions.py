# Python Functions
'''
1. Built-in Functions vs User Defined Functions
2. Arbitary Arguments (*args)
3. Keyword Arguments(**kwargs)
4. __doc__(docstrings)
'''

# UDF
'''
def greet(name):
    """ Greets a Person by name """
    return f"Hello , {name}! Welcome to the Python Classroom."

result = greet("Vivek")

print(greet("Samay"))
'''
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

def add(a , b):
    return a + b

print(add(10))
'''
# *args : Positional Arguments

def add_numbers(*args):
    """ Adds any number of arguments passed to it and return the total"""
    print("Type of args inside the function:" , type(args))
    total = 0
    for num in args:
        total += num
    return total


print(add_numbers())

# **kwargs : Keyword Arguments

def student_details(**kwargs):
    """Prints student details passed as keyword together in the same function."""
    print(type(kwargs))
    for key , value in kwargs.items():
        print(f"{key}  :{value}")

student_details(name="Rahul" , age = 20 , course = "Python")


def student_summary(*args , **kwargs):
    print("Positional args : " , args)
    print("Keyword args :" , kwargs)

student_summary("Python" , 85 , name="Rahul" , age = 20)


def display_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

my_list = [4 , 9 , 4 , 7 , 9 , 8]


print(display_list(my_list))


# Built-in function


my_list = [4 , 9 , 4 , 7 , 9 , 8]

print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sorted(my_list))
print(type(my_list))


