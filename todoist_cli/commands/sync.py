# commands/sync.py
from client import TodoistClient
from models.task import Task

def sync_tasks(api_token):
    client = TodoistClient(api_token)
    tasks_data = client.sync_tasks()
    if tasks_data:
        tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        print("Tasks synchronized:")
        for task in tasks:
            print(task)
    else:
        print("Failed to sync tasks.")
