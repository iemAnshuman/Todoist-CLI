import argparse
import os
from todoist_cli.commands import add, delete, list_task, sync
from dotenv import load_dotenv, set_key

load_dotenv()

API_TOKEN_ENV_VAR = "TODOIST_API_TOKEN"
ENV_FILE = ".env"

def get_api_token():
    api_token = os.getenv(API_TOKEN_ENV_VAR)
    if not api_token:
        api_token = input(f"Please enter your {API_TOKEN_ENV_VAR}: ")
        with open(ENV_FILE, 'a') as env_file:
            set_key(ENV_FILE, API_TOKEN_ENV_VAR, api_token)
    return api_token

def main():
    api_token = get_api_token()

    # Create the main parser
    parser = argparse.ArgumentParser(prog="todo", description="Todoist CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("content", help="Task content")
    parser_add.add_argument("--due", help="Due date")
    parser_add.add_argument("--priority", type=int, choices=[1, 2, 3, 4], help="Priority level")
    parser_add.add_argument("p", help="prompt") # incomplete

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", help="ID of the task")

    # List tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("--filter", help="Filter tasks")
    parser_list.add_argument("p", help="prompt") # incomplete

    # Sync tasks
    parser_sync = subparsers.add_parser("sync", help="Sync tasks")

    # Parse the arguments
    args = parser.parse_args()

    # Dispatch the command
    if args.command == "add":
        if args.p:
            args.due = input("Enter due date: ")
            args.priority = int(input("Enter priority level (1-4): "))
        add.add_task(api_token, args.content, args.due, args.priority)
    elif args.command == "delete":
        delete.delete_task(api_token, args.task_id)
    elif args.command == "list":
        if args.p:
            args.filter = input("Enter filter: ")
        list_task.list_tasks(api_token, args.filter)
    elif args.command == "sync":
        sync.sync_tasks(api_token)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

