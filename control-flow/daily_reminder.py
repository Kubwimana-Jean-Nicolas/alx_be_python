# daily_reminder.py

# Prompt user for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Determine time sensitivity
time_msg = "requires immediate attention today!" if time_bound == "yes" else "can be completed when convenient."

# Use Match Case to handle priority
match priority:
    case "high" | "medium" | "low":
        print(f"Reminder: '{task}' is a {priority} priority task that {time_msg}")
    case _:
        # Handle unexpected priority input
        print(f"Reminder: '{task}' is a task that {time_msg}")
