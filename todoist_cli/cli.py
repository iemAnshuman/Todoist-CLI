import argparse
import os
from todoist_cli.commands import add, delete, list_task, sync
from dotenv import load_dotenv, set_key
from rich import print
from rich.console import Console
from rich.table import Table
from todoist_cli.utils.catppuccin_theme import THEMES, get_theme
from todoist_cli.utils.config import set_selected_theme, get_selected_theme
# from todoist_cli.utils.ui_theme import display_task_list

# Initialize Rich Console and Theme
console = Console()
selected_theme = get_theme(get_selected_theme())

# Load environment variables from .env file
load_dotenv()

API_TOKEN_ENV_VAR = "TODOIST_API_TOKEN"
ENV_FILE = ".env"

def get_api_token():
    api_token = os.getenv(API_TOKEN_ENV_VAR)
    if not api_token:
        api_token = input(f"Please enter your {API_TOKEN_ENV_VAR}: ")
        set_key(ENV_FILE, API_TOKEN_ENV_VAR, api_token)
        load_dotenv()
        api_token = os.getenv(API_TOKEN_ENV_VAR)
    return api_token

def change_theme(args):
    theme_name = args.theme
    if theme_name in THEMES:
        set_selected_theme(theme_name)
        print(f"Theme changed to '{theme_name}'")
    else:
        print(f"Theme '{theme_name}' not found. Available themes: {', '.join(THEMES.keys())}")



def format_tasks(tasks):
    if not tasks:
        return {}
    tasks.sort(key=lambda x: (x.due_date or "", -x.priority))
    formatted_tasks = {}
    for task in tasks: 
        due_date = task.due_date or "No due date"
        if due_date not in formatted_tasks:
            formatted_tasks[due_date] = []
        formatted_tasks[due_date].append(task)
    return formatted_tasks

def display_tasks(formatted_tasks):
    for due_date, tasks in formatted_tasks.items():
        table = Table(title=f"[bold underline]{due_date}[/]", style=selected_theme['background'])
        table.add_column("ID", style=selected_theme['text'], justify="center")
        table.add_column("Content", style=selected_theme['text'])
        table.add_column("Due Date", style=selected_theme['highlight'])
        table.add_column("Priority", style=selected_theme['priority_1'])  # Default priority color
        table.add_column("Labels", style=selected_theme['text'])

        for task in tasks:
            priority_style = selected_theme.get(f"priority_{int(task.priority)}", selected_theme['text'])
            labels = ", ".join(task.labels) if task.labels else "None"
            table.add_row(
                str(task.id),
                task.content,
                task.due_date or "No due date",
                f"[{priority_style}]{task.priority}[/{priority_style}]",
                labels
            )

        console.print(table)

def main():
    # Ensure API token is set
    api_token = get_api_token()

    # Create the main parser
    parser = argparse.ArgumentParser(prog="todo", description="Todoist CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("content", help="Task content")
    parser_add.add_argument("--due", help="Due date")
    parser_add.add_argument("--priority", type=int, choices=[1, 2, 3, 4], help="Priority level")
    parser_add.add_argument("--labels", help="Labels (comma-separated)")
    parser_add.add_argument("-p", "--prompt", action="store_true", help="Prompt for task details interactively")    

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", help="ID of the task")

    # List tasks with specific filters
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("--due", help="Filter by due date (e.g., 'today', 'tomorrow')")
    parser_list.add_argument("--priority", type=int, choices=[1, 2, 3, 4], help="Filter by priority")
    parser_list.add_argument("--project", help="Filter by project name")
    parser_list.add_argument("--label", help="Filter by label name") 
    parser_list.add_argument("-p", "--prompt", action="store_true", help="Prompt for filter details interactively")

    # Change theme
    parser_theme = subparsers.add_parser("theme", help="Change the theme")
    parser_theme.add_argument("theme", help="Name of the theme to set")
    parser_theme.set_defaults(func=change_theme)

    # Sync tasks
    parser_sync = subparsers.add_parser("sync", help="Sync tasks")

    # Parse the arguments
    args = parser.parse_args()

    # Dispatch the command
    if args.command == "add":
        if args.prompt:
            args.content = input("Enter task content: ")
            args.due = input("Enter due date: ")
            args.priority = input("Enter priority level (1-4): ")
            if args.priority and args.priority in ['1', '2', '3', '4']:
                args.priority = int(args.priority)
            args.labels = input("Enter labels (comma-separated): ").split(",")
        add.add_task(api_token, args.content, args.due, args.priority, args.labels)
    elif args.command == "delete":
        delete.delete_task(api_token, args.task_id)
    elif args.command == "list":
        if args.prompt:
            args.due = input("Enter due date: ")
            args.priority = (input("Enter priority level (1-4): "))
            if args.priority and args.priority in ['1', '2', '3', '4']:
                args.priority = int(args.priority)
            args.project = input("Enter project name: ")
            args.label = input("Enter label name: ")
        if args.due == "today":
            args.due = "today | overdue"
        tasks = list_task.list_tasks(api_token, args)
        display_tasks(format_tasks(tasks))
    elif args.command == "sync":
        sync.sync_tasks(api_token)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
