# Sets , Dictionary  , Type Conversion  , List of Disctionary

# A set is a collection data type in python that stores unique values.It does not allow duplicate values.

# A Dictionary is a collection data type that stores data in key-value pairs.

# Type conversion is the process of converting a value from one data type to another data type.

# A List of Dictionares is a list that contains multiple dictionares as its element.

print("=" * 40)

print("01. Set")

numbers = {1 , 2 , 3 , 4 , 5 , 5 , 1}

print(numbers)

numbers.add(6)

print(numbers)

numbers.remove(3)

print(numbers)

print(3 in numbers)
print(2 in numbers)


# Dictionary

print("=" * 40)
print("02. Dictionary")

student = {
    "name":"Rahul",
    "age":20,
    "grade":"A"
}

print(student["name"])

for key in student.keys():
    print(f"{key} : {student[key]}")

for value in student.values():
    print(value)

student["city"] = "Surat"

student["age"] = 25

print(student)

# Dictionary from lists

print("=" * 40)

key = ["id" , "name" , "email"]
value = [101 , "Rakesh" , "rakesh@gmail.com"]

print(len(key))

print(key , value)

employee = {}

for i in range(len(key)):
    employee[key[i]] = value[i]

print(employee)

# Type Conversion

print("=" * 40)

num = "123"
print(type(num))
print(type(int(num)))

list1 = [1 , 2 , 3 , 4]
tuple1 = tuple(list1)
print(list1)
print(tuple1)

pairs = [(1 , "Apple") , (2 , "Mango")]

dict1 = dict(pairs)

print(dict1)

# Delete item using del keyword

numbers = [10 , 20 , 30 , 40 , 50]
print(numbers)

del numbers[0]

print(numbers)









