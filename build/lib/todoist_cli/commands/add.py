# commands/add.py
from todoist_cli.client import TodoistClient

def add_task(api_token, content, due_string=None, priority=1):
    client = TodoistClient(api_token)
    task = client.add_task(content, due_string, priority)
    if task:
        print(f"Task '{task['content']}' added with ID: {task['id']}")
    else:
        print("Failed to add task.")

