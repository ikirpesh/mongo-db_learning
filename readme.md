# 🎓 Student Management System using Python & MongoDB

A simple command-line **Student Management System** built using **Python** and **MongoDB**.

I created this project while learning MongoDB to understand how Python applications can connect to and perform CRUD operations on a MongoDB database.

## 🚀 Features

* ➕ Add new students
* 🔍 Search students by:

  * Name
  * Roll Number
  * Date of Birth
* ✏️ Update student details

  * Name
  * Date of Birth
* 🗑️ Delete student records
* 🍃 Store and manage student data using MongoDB

## 🛠️ Technologies Used

* Python
* MongoDB
* PyMongo
* MongoDB Compass

## 📂 Database Structure

**Database**
`student_registration`

**Collection**
`students_details`

Example document:

```json
{
  "id": 101,
  "name": "Student Name",
  "dob": 20080115
}
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ikirpesh/mongo-db_learning.git
cd mongo-db_learning
```

### 2. Install PyMongo

```bash
pip install pymongo
```

### 3. Start MongoDB

Make sure MongoDB is running locally on:

```text
mongodb://localhost:27017/
```

### 4. Run the program

```bash
python student_marks.py
```

## 💻 Program Menu

When the program starts, you can choose from:

```text
Welcome to Student Management System

1. Add Student
2. Search Details
3. Update Student Details
4. Delete a Student
```

## 📚 What I Learned

Through this project, I learned how to:

* Connect Python with MongoDB using PyMongo
* Create and work with MongoDB databases and collections
* Insert documents into MongoDB
* Search and filter documents
* Use MongoDB regular expressions for name searches
* Update existing documents
* Delete documents
* Perform CRUD operations using Python
* View and manage data through MongoDB Compass

## 🔮 Future Improvements

I plan to improve this project by adding:

* Better input validation and error handling
* Duplicate roll-number checking
* Improved command-line interface
* Student marks and subject management
* Automatic grade calculation
* A GUI or web-based interface

## 👨‍💻 Author

**Kirpesh**

GitHub: https://github.com/ikirpesh

## 📜 About

This project was created as part of my journey learning **MongoDB and database integration with Python**.

⭐ If you find this project useful, feel free to star the repository!
