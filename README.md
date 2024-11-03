# Todoist CLI Tool

A simple command-line interface (CLI) tool for managing Todoist tasks. With this tool, you can easily add, delete, list, and sync your tasks from the command line.

## Features

- Add tasks with optional due dates and priority levels.
- Delete tasks by ID.
- List tasks with filtering options.
- Sync tasks with your Todoist account.

## Installation

To install the Todoist CLI, you need Python 3.6 or later. You can install it via pip:

```bash
pip install cli-tool-for-todoist==0.1
```

## Usage

After installation, you can use the following commands in your terminal:

### Add a Task

```bash
todo-add "Task description" --due "2024-11-05" --priority 2
```

### Delete a Task

```bash
todo-delete <task_id>
```

### List Tasks

```bash
todo-list --filter "today"
```

### Sync Tasks

```bash
todo-sync
```

## Command Options

- **todo-add**
  - `content`: The content of the task (required).
  - `--due`: Optional due date for the task.
  - `--priority`: Optional priority level (1-4).

- **todo-delete**
  - `task_id`: The ID of the task you want to delete (required).

- **todo-list**
  - `--filter`: Optional filter to show specific tasks.

- **todo-sync**
  - Syncs local tasks with your Todoist account.

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Todoist API](https://developer.todoist.com/) to manage tasks.

## Contact

For questions or suggestions, feel free to reach out to the author:

- Name: Anshuman Agrawal
- Email: asquare567@gmail.com
- Website: [asquare.site](https://www.asquare.site)

---

Enjoy managing your tasks with Todoist CLI!
