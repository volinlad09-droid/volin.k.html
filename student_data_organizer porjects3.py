"""
Project: Collection Manipulator / Student Data Organizer

This program demonstrates:
- String formatting and manipulation
- List, Tuple, Set, and Dictionary collections
- List mutability and Tuple immutability
- Type casting
- The del keyword
- type() and id()
"""

from datetime import datetime


def show_variable(name, value):
    """Display a value, its type, and memory address."""
    print(
        f"{name}: {value} "
        f"(Type: {type(value)}, Memory Address: {id(value)})"
    )


def main():
    print("=" * 65)
    print("Welcome to the Student Data Organizer!")
    print("This program collects personal information and manages")
    print("student records using Python collection data types.")
    print("=" * 65)

    # ------------------------------------------------------------
    # Part 1: Collect personal information and demonstrate casting
    # ------------------------------------------------------------
    name = input("\nPlease enter your name: ").strip()

    age_text = input("Please enter your age: ").strip()
    age = int(age_text)

    height_text = input("Please enter your height in meters: ").strip()
    height = float(height_text)

    favourite_number_text = input("Please enter your favourite number: ").strip()
    favourite_number = int(favourite_number_text)

    current_year = datetime.now().year
    birth_year = current_year - age

    print("\nThank you! Here is the information we collected:")
    print("-" * 65)

    # f-string formatting
    show_variable("Name", name)
    # .format() formatting
    print(
        "Age: {} (Type: {}, Memory Address: {})".format(
            age, type(age), id(age)
        )
    )
    # % formatting
    print(
        "Height: %s (Type: %s, Memory Address: %s)"
        % (height, type(height), id(height))
    )
    show_variable("Favourite Number", favourite_number)

    print(
        "\nYour birth year is approximately: "
        f"{birth_year} (based on your age of {age})"
    )

    print("\nType Casting Demonstration:")
    print(f"Age input '{age_text}' changed from str to int -> {age}")
    print(f"Height input '{height_text}' changed from str to float -> {height}")
    print(
        f"Favourite number input '{favourite_number_text}' "
        f"changed from str to int -> {favourite_number}"
    )

    # ------------------------------------------------------------
    # Part 2: Student collection manipulator
    # ------------------------------------------------------------
    print("\n" + "=" * 65)
    print("Student Record Manager")
    print("=" * 65)

    student_records = []       # LIST: multiple student records
    student_lookup = {}        # DICTIONARY: ID -> student data
    unique_subjects = set()    # SET: subjects without duplicates

    while True:
        print("\nEnter student details.")
        student_id = input("Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            continue

        if student_id in student_lookup:
            print("That Student ID already exists. Please use another ID.")
            continue

        student_name = input("Student name: ").strip()

        student_age = int(input("Student age: ").strip())
        grade = input("Grade/Class: ").strip()

        dob = input("Date of birth (DD-MM-YYYY): ").strip()
        subjects_text = input(
            "Subjects (comma-separated; duplicates are removed): "
        ).strip()

        subjects = [
            subject.strip()
            for subject in subjects_text.split(",")
            if subject.strip()
        ]

        # TUPLE: immutable student ID + date of birth
        fixed_info = (student_id, dob)

        # Dictionary containing the student's details
        student_data = {
            "name": student_name,
            "age": student_age,
            "grade": grade,
            "subjects": subjects,
            "fixed_info": fixed_info,
        }

        # LIST: store each complete student record
        student_record = [student_id, student_name, student_age, grade, subjects]
        student_records.append(student_record)

        # DICTIONARY: use Student ID as key
        student_lookup[student_id] = student_data

        # SET: keep subjects unique
        unique_subjects.update(subjects)

        print("\nStudent added successfully.")

        more = input("Add another student? (y/n): ").strip().lower()
        if more != "y":
            break

    # ------------------------------------------------------------
    # Part 3: Demonstrate list mutability
    # ------------------------------------------------------------
    if student_records:
        print("\n" + "-" * 65)
        print("List Mutability Demonstration")
        print("-" * 65)

        old_grade = student_records[0][3]
        student_records[0][3] = f"{old_grade} (Updated)"

        print("The first student's grade was modified in the list.")
        print(f"Old grade: {old_grade}")
        print(f"New grade: {student_records[0][3]}")

        # Keep the dictionary synchronized with the modified list
        first_id = student_records[0][0]
        student_lookup[first_id]["grade"] = student_records[0][3]

    # ------------------------------------------------------------
    # Part 4: Demonstrate tuple immutability
    # ------------------------------------------------------------
    print("\n" + "-" * 65)
    print("Tuple Immutability Demonstration")
    print("-" * 65)

    if student_lookup:
        first_student = next(iter(student_lookup.values()))
        fixed_info = first_student["fixed_info"]

        print(f"Fixed information tuple: {fixed_info}")
        print(
            "Tuples are immutable, so the Student ID and Date of Birth "
            "are intended to remain unchanged."
        )

        try:
            fixed_info[0] = "CHANGED"
        except TypeError:
            print("Attempting to change the tuple raises TypeError.")

    # ------------------------------------------------------------
    # Part 5: Display collections
    # ------------------------------------------------------------
    print("\n" + "=" * 65)
    print("Final Collection Summary")
    print("=" * 65)

    print("\n1. LIST - Student records:")
    for record in student_records:
        print(record)

    print("\n2. TUPLE - Fixed student information:")
    for sid, details in student_lookup.items():
        print(f"{sid}: {details['fixed_info']}")

    print("\n3. SET - Unique subjects:")
    print(sorted(unique_subjects))

    print("\n4. DICTIONARY - Student data:")
    for sid, details in student_lookup.items():
        print(
            f"\nStudent ID: {sid}\n"
            f"Name: {details['name']}\n"
            f"Age: {details['age']}\n"
            f"Grade: {details['grade']}\n"
            f"Subjects: {', '.join(details['subjects']) or 'None'}\n"
            f"Fixed Info: {details['fixed_info']}"
        )

    # ------------------------------------------------------------
    # Part 6: del keyword demonstration
    # ------------------------------------------------------------
    print("\n" + "-" * 65)
    print("del Keyword Demonstration")
    print("-" * 65)

    if student_records:
        deleted_demo_record = student_records.pop()
        print(
            "Removed the last record from the working list using "
            "list.pop() for a safe demonstration."
        )
        student_records.append(deleted_demo_record)

    # Demonstrate del on a temporary variable without removing real data
    temp_data = {"example": "temporary value"}
    del temp_data["example"]
    print("Used del to remove a temporary dictionary item.")

    # ------------------------------------------------------------
    # Part 7: Friendly formatted output
    # ------------------------------------------------------------
    print("\n" + "=" * 65)
    print("Student Data Organizer Report")
    print("=" * 65)

    for sid, details in student_lookup.items():
        print(f"\nStudent ID : {sid}")
        print(f"Name       : {details['name'].title()}")
        print(f"Age        : {details['age']}")
        print(f"Grade      : {details['grade']}")
        print(f"Subjects   : {', '.join(details['subjects']) or 'None'}")
        print(f"Fixed Info : {details['fixed_info']}")

    print("\nTotal students:", len(student_records))
    print("Total unique subjects:", len(unique_subjects))

    print("\nThank you for using the Student Data Organizer!")
    print("Keep practicing Python and explore more collection features.")


if __name__ == "__main__":
    main()
