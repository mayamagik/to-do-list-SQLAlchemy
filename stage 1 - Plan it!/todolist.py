# To-Do List Stage 1: Task management

today = ["Do yoga", "Make a breakfast", "Learn the basics of SQL", "Learn about ORM"]

def today_tasks(day, activities):
      print(f"{day}:")

      for number, activity in enumerate(activities, start=1):
            print(f"{number}) {activity}")


today_tasks("Today", today)
