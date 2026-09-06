# 📚 Library Book Management System

## 📌 Project Overview
The **Library Book Management System** is a Python-based, menu-driven console application designed to help librarians efficiently manage book records. The system allows users to **add, update, remove, search, sort, and analyze books** stored in the library.

This project is built to demonstrate core **Python programming concepts** including **Object-Oriented Programming (OOP)**, **functions**, **loops**, **control structures**, **collections**, **sorting**, and **input validation**.

---

## 🎯 Objectives
- Manage library books effectively
- Demonstrate fundamental and advanced Python concepts
- Build a real-world, menu-driven application
- Ensure proper input validation and data handling

---

## 🛠️ Features
- ➕ Add a new book
- 📖 View all books
- ✏️ Update book information (title, author, copies)
- ❌ Remove a book
- 🔍 Search books by title or author
- 🔃 Sort books by title or available copies
- 📊 Display library statistics
- 🚪 Exit the program

---

## 📂 Data Structure
Each book record contains the following details:
- **Book ID** (Integer – Unique)
- **Title** (String)
- **Author** (String)
- **Copies Available** (Integer – Non-negative)

Books are stored using a **list of Book objects**.

---

## 🧠 Concepts Used

### ✅ Python Fundamentals
- Variables & Datatypes
- Type Casting (`int()`)
- Operators
- Input/Output operations

### ✅ Control Flow
- `if-else` statements
- Menu-based decision handling

### ✅ Looping
- `while` loop for menu navigation
- `for` loops for iterating over book records

### ✅ Collections
- `list` to store multiple book objects

### ✅ Functions
- Modular functions for each operation

### ✅ Sorting
- Built-in `sorted()` function
- Sorting using `lambda` expressions

### ✅ Object-Oriented Programming (OOP)
- `Book` class to represent book details
- `Library` class to manage operations

---

## 🧾 Program Structure

```
Library_Book_Management_System/
│
├── library.py        # Main Python program
└── README.md         # Project documentation
```

---

## ▶️ How to Run the Program
1. Install **Python 3.x** on your system
2. Save the program file as `library.py`
3. Open terminal / command prompt
4. Navigate to the project folder
5. Run the command:

```
python library.py
```

---

## 🖥️ Sample Menu Output
```
====== Library Book Management System ======
1. Add Book
2. View All Books
3. Update Book
4. Remove Book
5. Search Book
6. Sort Books
7. Library Statistics
0. Exit
```

---

## 🔐 Input Validation Rules
- Book ID must be **unique**
- Number of copies must be a **non-negative integer**
- Invalid menu selections are handled safely

---

## 🚀 Future Enhancements
- File handling using **CSV / JSON** for data persistence
- User authentication (Admin / Librarian)
- GUI version using **Tkinter** or **PyQt**
- Database integration (MySQL / SQLite)

---

## 👨‍💻 Author
Python Developer | Student

---

## 📄 License
This project is created for **educational purposes** and is free to use and modify.

---

✨ *Happy Coding!* ✨

