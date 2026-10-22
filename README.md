# To-Do List (Python)

A command-line task manager built with Python, SQLite, and SQLAlchemy as part of the Hyperskill To-Do List (Python) project. The application stores tasks with deadlines, displays tasks by date, identifies overdue tasks, and lets users delete tasks.

## Features

- Add tasks with a deadline in `YYYY-MM-DD` format
- View tasks due today
- View tasks for the next seven days
- View all tasks ordered by deadline
- View missed (overdue) tasks
- Delete a task by selecting its number from a sorted list
- Persist tasks in a local SQLite database using SQLAlchemy

## Project development

| Stage | What was implemented |
| --- | --- |
| 1 — Basic to-do list | A simple interactive command-line menu for managing tasks. |
| 2 — Data persistence | SQLite storage through SQLAlchemy, including a task model, database session, and adding/retrieving tasks. |
| 3 — Deadlines | A deadline field, date parsing, and views for today's tasks, the next seven days, and all tasks sorted by deadline. |
| 4 — Missed tasks and deletion | Filtering tasks with expired deadlines and deleting a selected task from the database. |

## Technologies

- Python 3
- SQLite
- SQLAlchemy ORM
- Python's built-in `datetime` module

## Getting started

1. Make sure Python 3 is installed.
2. Install SQLAlchemy:

   `python -m pip install SQLAlchemy`

3. Open a terminal in the folder containing `todolist.py` and run:

   `python todolist.py`

The application uses a local SQLite database (`todo.db`). Because the connection uses a relative database path, the database file is created or opened in the terminal's current working directory.

The complete application is in `stage 4/todolist/todolist.py`, with earlier stages documenting its development.

## Menu

```text
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task
6) Delete a task
0) Exit
```

When adding a task, enter the deadline as `YYYY-MM-DD`. To delete a task, choose its number from the displayed list.

## What I practiced

- Defining an ORM model and creating database tables
- Querying, filtering, and sorting records with SQLAlchemy
- Adding and deleting records with database sessions and commits
- Comparing and formatting dates with `datetime` and `timedelta`
- Building an interactive command-line
