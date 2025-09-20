# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

time_msg = "requires immediate attention today!" if time_bound == "yes" else "can be completed when convenient."

match priority:
    case "high" | "medium" | "low":
        print(f"Reminder: {task} is a {priority} priority task that {time_msg}")
    case _:
        print(f"Reminder: {task} is a task that {time_msg}")
