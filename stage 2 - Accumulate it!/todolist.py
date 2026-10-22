# To-Do List Stage 2: SQLite database integration with SQLAlchemy
"""Steps:
        1. Imports
        2. Database setup — engine and Base
        3. Table definition — class Table(Base)
        4. Table creation — Base.metadata.create_all(engine)
        5. Session setup — sessionmaker() and session
        6. Database functions — add_task() and display_tasks()
        7. Menu function — todo_menu()
        8. Program entry point — if __name__ == "__main__":
"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date
from datetime import datetime

# Create and connect db
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Create declarative base
Base = declarative_base()

# Define table
class Table(Base):
      __tablename__ = 'task'
      id = Column(Integer, primary_key=True)
      task = Column(String, default='default_value')
      deadline = Column(Date, default=datetime.today())

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

# Create add_task
def add_task():
    print("Enter a task:")
    task_choice = input()

    new_task = Table(task=task_choice)

    session.add(new_task)
    session.commit()

    print("The task has been added!")

# Create display_tasks
def display_tasks():
    rows = session.query(Table).all()

    if rows:
        print(f"Today:")

        for number, row in enumerate(rows, start=1):
            print(f"{number}. {row.task}")
    else:
        print("Nothing to do!")

# Create display menu
def todo_menu():

      while True:
            print ()
            print("1) Today's tasks\n"
                  "2) Add a task\n"
                  "0) Exit")

            choice = int(input())

            if choice == 1:
                 display_tasks()
            elif choice == 2:
                  add_task()
            elif choice == 0:
                  print("Bye!")
                  break

# Call menu
if __name__ == "__main__":
    todo_menu()