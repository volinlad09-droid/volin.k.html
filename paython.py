# PR. 3 - Collection Manipulator
# Python Program

def collection_manipulator():
    print("====================================")
    print("       COLLECTION MANIPULATOR")
    print("====================================")

    # List
    numbers = [10, 20, 30, 40, 50]

    print("\nOriginal List:", numbers)

    numbers.append(60)
    print("After append(60):", numbers)

    numbers.remove(20)
    print("After remove(20):", numbers)

    numbers.sort(reverse=True)
    print("After sorting descending:", numbers)

    # Tuple
    fruits = ("Apple", "Banana", "Mango", "Orange")

    print("\nOriginal Tuple:", fruits)
    print("First fruit:", fruits[0])
    print("Number of fruits:", len(fruits))

    # Set
    colors = {"Red", "Green", "Blue"}

    print("\nOriginal Set:", colors)

    colors.add("Yellow")
    print("After adding Yellow:", colors)

    colors.remove("Green")
    print("After removing Green:", colors)

    # Dictionary
    student = {
        "name": "Rahul",
        "age": 18,
        "course": "Python"
    }

    print("\nOriginal Dictionary:", student)

    student["city"] = "Surat"
    print("After adding city:", student)

    student["age"] = 19
    print("After updating age:", student)

    print("Student Name:", student["name"])

    # Final Output
    print("\n====================================")
    print("       FINAL COLLECTIONS")
    print("====================================")
    print("List       :", numbers)
    print("Tuple      :", fruits)
    print("Set        :", colors)
    print("Dictionary :", student)


# Run program
collection_manipulator()