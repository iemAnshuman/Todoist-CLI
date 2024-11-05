# commands/list_tasks.py
from todoist_cli.client import TodoistClient
from todoist_cli.models.task import Task

def list_tasks(api_token, args):
    client = TodoistClient(api_token)

    # Build the filter string based on provided arguments
    filter_components = []
    if args.due:
        filter_components.append(f'due:{args.due}')
    if args.priority:
        filter_components.append(f'priority:{args.priority}')
    if args.project:
        filter_components.append(f'##{args.project}')
    if args.label:
        filter_components.append(f'@{args.label}')

    filter_string = ' & '.join(filter_components) if filter_components else None

    # Fetch tasks using the constructed filter string
    tasks_data = client.list_tasks(filter_string)
    if tasks_data:
        tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        return tasks
    else:
        print("No tasks found.")
        return []