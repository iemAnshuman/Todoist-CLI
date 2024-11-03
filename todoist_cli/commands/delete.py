# commands/delete.py
from todoist_cli.client import TodoistClient

def delete_task(api_token, task_id):
    client = TodoistClient(api_token)
    if client.delete_task(task_id):
        print(f"Task with ID '{task_id}' deleted successfully.")
    else:
        print(f"Failed to delete task with ID '{task_id}'.")
