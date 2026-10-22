# To-Do List Stage 4: Missed Tasks and Task Deletion
"""Steps:
New functionality:
    1. missed_tasks():
       - Display tasks with deadlines earlier than today
       - Sort overdue tasks chronologically
       - Handle cases where no overdue tasks exist

    2. delete_tasks():
       - Display all tasks sorted by deadline
       - Allow users to select a task by its number
       - Delete the selected record from the SQLite database
       - Commit changes to ensure permanent deletion

    3. Updated menu:
       - Option 4: Missed tasks
       - Option 
    - Select tasks for deletion using numbered lists
    - Format dates for readable console output
    - Navigate through an interactive command-line menu
"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date
from datetime import datetime, timedelta

# Create and connect db
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Create declarative base
Base = declarative_base()

# Define table
class Table(Base):
      __tablename__ = 'task'
      id = Column(Integer, primary_key=True)
      task = Column(String, default='default_value')
      deadline = Column(Date)

      def __repr__(self):
            return self.string_field

# Add table to db
Base.metadata.create_all(engine)

# Access db
Session = sessionmaker(bind=engine)
session = Session()

# Check if table exists in db
# inspector = inspect(engine)
# print(inspector.get_table_names())

# Create add_task & add deadline
def add_task():
    print("Enter a task")
    task_choice = input()

    # Add deadline
    print("Enter a deadline")
    deadline_choice = input()
    deadline = datetime.strptime(deadline_choice, "%Y-%m-%d").date()

    new_task = Table(
          task=task_choice,
          deadline=deadline,)

    session.add(new_task)
    session.commit()

    print("The task has been added!")

# Create display_week_tasks()
def display_week_tasks():
      today = datetime.today().date()

      # Display days starting today
      for i in range(7):
            day = today + timedelta(days=i)

            # Query tasks for this day
            rows = session.query(Table).filter(Table.deadline == day).all()

            print()
            # Convert day to str and print as 'Monday 10 Oct'
            print(f"{day.strftime('%A')} {day.day} {day.strftime('%b')}:")

            if rows:
                  for number, row in enumerate(rows, start=1):
                        print(f"{number}. {row.task}")
            else:
                  print("Nothing to do!")

# Create display_today_tasks & filter today-deadlines
def display_today_tasks():
    today = datetime.today().date()
    rows = session.query(Table).filter(Table.deadline == today).all()

    # Convert today object to str and print it as '22 Oct'
    print(f"{today.day} {today.strftime('%b')}")

    if rows:
        for number, row in enumerate(rows, start=1):
            print(f"{number}. {row.task}")
    else:
        print("Nothing to do!")

# Create display_all_tasks
def display_all_tasks():
    rows = session.query(Table).order_by(Table.deadline).all()

    print("All tasks:")

    if rows:
        for number, row in enumerate(rows, start=1):
            print(f"{number}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")
    else:
        print("Nothing to do!")

# Create missed_tasks
def missed_tasks():
    today = datetime.today().date()

    rows = (session.query(Table).filter(Table.deadline < today).
            order_by(Table.deadline).all())

    print("Missed tasks:")

    if rows:
        for number, row in enumerate(rows, start=1):
            print(f"{number}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")
    else:
        print("All tasks have been completed!")

# Create delete tasks
def delete_tasks():
    rows = session.query(Table).order_by(Table.deadline).all()

    if not rows:
        print("Nothing to delete")
    else:
        print("Choose the number of the task you want to delete:")

        for number, row in enumerate(rows, start=1):
            print(f"{number}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}")

        task_to_delete = int(input())

        specific_row = rows[task_to_delete - 1]
        session.delete(specific_row)
        session.commit()

        print("The task has been deleted!")

# Create display menu
def todo_menu():

      while True:
            print ()
            print("1) Today's tasks\n"
                  "2) Week's tasks\n"
                  "3) All tasks\n"
                  "4) Missed tasks\n"
                  "5) Add a task\n"
                  "6) Delete a task\n"
                  "0) Exit")

            choice = int(input())

            if choice == 1:
                 display_today_tasks()
            elif choice == 2:
                  display_week_tasks()
            elif choice == 3:
                  display_all_tasks()
            elif choice == 4:
                  missed_tasks()
            elif choice == 5:
                add_task()
            elif choice == 6:
                delete_tasks()
            elif choice == 0:
                  print("Bye!")
                  break

# Call menu
if __name__ == "__main__":
    todo_menu()
