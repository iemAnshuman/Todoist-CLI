# commands/list_task.py
from todoist_cli.client import TodoistClient
from todoist_cli.models.task import Task
from todoist_cli.utils.catppuccin_theme import apply_catppuccin_theme

theme = apply_catppuccin_theme()

def list_tasks(api_token, filter=None):
    client = TodoistClient(api_token)
    tasks_data = client.list_tasks(filter)
    if tasks_data:
        tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        for task in tasks:
            # Assign colors based on priority
            color = theme[f"priority_{task.priority}"]
            background = theme["background"]
            text_color = theme["text"]

            # Use ANSI escape codes for color formatting in the terminal
            print(f"\033[38;5;{color}m \0{task.content}\033[0m")  # Text color

            # Example: Customize further if needed
            # print(f"{task.priority}: {task.content} - Due: {task.due_date}")
    else:
        print("No tasks found or failed to retrieve tasks.")

