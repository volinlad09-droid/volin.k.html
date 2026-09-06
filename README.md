# Collection Manipulator / Student Data Organizer

## Project: Collection Manipulator / Student Data Organizer

### Objective
This Python project, **Student Data Organizer**, manages student records while demonstrating intermediate Python concepts:

- String formatting and manipulation
- List
- Tuple
- Set
- Dictionary
- Mutability and immutability
- Type casting
- `del` keyword
- `type()` and `id()`

## Features

The program first collects:

- Name (`str`)
- Age (`int`)
- Height (`float`)
- Favourite number (`int`)

It then calculates an approximate birth year and displays each value, its data type, and memory address.

The student-record section collects:

- Student ID
- Student name
- Age
- Grade
- Date of birth
- Subjects

### Collection usage

**List:** Stores multiple student records.

**Tuple:** Stores the Student ID and Date of Birth as fixed information. Tuples are immutable.

**Set:** Stores unique subjects and automatically removes duplicates.

**Dictionary:** Uses Student ID as the key and stores each student's details as another dictionary.

### Mutability and immutability

A student's grade in the list is modified to demonstrate list mutability.

The tuple containing Student ID and Date of Birth is kept unchanged. An attempted tuple modification is included to demonstrate that Python raises `TypeError`.

### Type casting

`input()` initially returns strings. The program converts:

- Age using `int()`
- Height using `float()`
- Favourite number using `int()`

### `del` keyword

The program uses `del` on a temporary dictionary item to demonstrate deletion without affecting the main student database.

## Assumptions

1. Age is entered as a whole number.
2. Height is entered in meters.
3. Favourite number is an integer.
4. Date of birth is entered in `DD-MM-YYYY` format.
5. Student IDs must be unique.
6. Subjects are entered as comma-separated text.
7. The birth year is an approximation based only on the current year minus age; the exact birth year depends on whether the birthday has occurred this year.
8. The program is intended to run in a standard Python 3 environment.

## How to Run

Open a terminal in this project folder and run:

```bash
python student_data_organizer.py
```

## Example

The program begins with a welcome message, asks for personal information, demonstrates type casting and formatting, then collects student records and prints the final collection summary.

## Files

- `student_data_organizer.py` - Main Python source code
- `README.md` - Project documentation

## GitHub Submission

Create a GitHub repository, for example:

`student-data-organizer`

Then upload:

- `student_data_organizer.py`
- `README.md`

After pushing the files, copy the repository URL and submit it to your instructor.

## Originality

This project is written specifically for this assignment. Students should review, understand, and adapt the code in their own words and according to their instructor's requirements before submission.
