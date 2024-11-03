# commands/list.py
from client import TodoistClient
from models.task import Task

def list_tasks(api_token, filter=None):
    client = TodoistClient(api_token)
    tasks_data = client.list_tasks(filter)
    if tasks_data:
        tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        for task in tasks:
            print(task)
    else:
        print("No tasks found or failed to retrieve tasks.")
