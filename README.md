# 📝 To-Do List Manager

A professional command-line **To-Do List Manager** built with **Python**. This application helps users efficiently manage daily tasks with features like adding, viewing, editing, deleting, searching, and marking tasks as completed. All tasks are stored permanently using a JSON file.

---

## 🚀 Features

- ➕ Add new tasks
- 📋 View all tasks
- ✏️ Edit existing tasks
- ❌ Delete tasks
- ✅ Mark tasks as completed
- 🔍 Search tasks by keyword
- 📊 View task statistics
- 💾 Automatic data persistence using JSON
- 🛡️ Input validation and exception handling
- 📂 Modular project structure

---

## 📂 Project Structure

```
ToDoList/
│
├── main.py              # Entry point of the application
├── task_manager.py      # Business logic
├── file_handler.py      # JSON file operations
├── utils.py             # Utility functions
├── todo.json            # Stores all tasks
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3.x
- JSON
- OS Module

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/todo-list-manager.git
```

### 2. Navigate to the project

```bash
cd todo-list-manager
```

### 3. Run the application

```bash
python main.py
```

---

## 📌 Menu

```
========================================
         TO-DO LIST MANAGER
========================================

1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Edit Task
6. Search Task
7. Statistics
8. Exit

========================================
```

---

## 📷 Sample Output

```
========== YOUR TASKS ==========

ID : 1
Task : Study Python
Status : ✖
-----------------------------------

ID : 2
Task : Complete DecodeLabs Project
Status : ✔
-----------------------------------
```

---

## 💾 Data Storage

All tasks are stored in:

```
todo.json
```

Example:

```json
[
    {
        "id": 1,
        "title": "Study Python",
        "completed": false
    },
    {
        "id": 2,
        "title": "Complete DecodeLabs Project",
        "completed": true
    }
]
```

---

## 📚 Concepts Covered

This project demonstrates:

- Variables
- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Exception Handling
- File Handling
- JSON
- Modular Programming
- Code Reusability

---

## 🎯 Future Improvements

- 📅 Due Dates
- ⭐ Task Priorities
- 🗂️ Categories
- 🌙 Dark Mode UI
- 🎨 Colored Terminal Output
- 📈 Progress Dashboard
- 🔐 User Authentication
- 🖥️ GUI Version (Tkinter/PyQt)
- 🌐 Web Version (Flask/Django)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👩‍💻 Author

**Priyanshi Goyal**

- GitHub: https://github.com/Priyanshi00Goyal
- LinkedIn: https://www.linkedin.com/in/priyanshi-goyal-a72b42379

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider giving it a **star** on GitHub!
