# Todoist CLI Tool

A command-line interface (CLI) for managing tasks on Todoist. This tool allows you to add, delete, list, and sync tasks directly from your terminal.

## Features

- **Add tasks** with optional due dates, priority levels, and labels.
- **Delete tasks** by ID.
- **List tasks** with filters for due dates, priority, projects, or labels.
- **Sync tasks** with your Todoist account.
- **Customizable themes** for personalized task displays in the terminal.

## Installation

To install the Todoist CLI, you need Python 3.6 or later. Install it via pip:

```bash
pip install cli-tool-for-todoist
```

## Usage

After installation, use the following commands in your terminal:

### Add a Task

```bash
todo add "Task description" --due "2024-11-05" --priority 2
```

### Delete a Task

```bash
todo delete <task_id>
```

### List Tasks

```bash
todo list --due "today"
```

### Sync Tasks

```bash
todo sync
```

### Change Theme

```bash
todo theme <theme_name>
```

Available themes include `catppuccin`, `solarized`, and more.

## Command Options

### todo add
- `content`: The content of the task (required).
- `--due`: Optional due date (e.g., `today`, `tomorrow`, or a specific date).
- `--priority`: Optional priority level (1-4).
- `--labels`: Optional labels, comma-separated.
- `-p`, `--prompt`: Interactively prompt for task details.

### todo delete
- `task_id`: The ID of the task to delete (required).

### todo list
- `--due`: Filter by due date.
- `--priority`: Filter by priority level (1-4).
- `--project`: Filter by project name.
- `--label`: Filter by label.
- `-p`, `--prompt`: Interactively prompt for filter options.

### todo theme
- `theme_name`: Name of the theme to set.

### todo sync
- Sync tasks with your Todoist account.

## Enhancements for Usability

This CLI is still in development and may need improvements to enhance user experience. Here are a few suggestions:

1. **Error Handling**: Provide clear error messages when API calls fail, and suggest possible fixes.
2. **Interactive Prompts**: For all commands, add prompts that guide users through options like task content, due dates, and priority levels.
3. **Help Descriptions**: Add detailed help descriptions for each command option. This could include examples or notes about required vs. optional parameters.
4. **Theme Preview**: Allow users to preview themes before selecting them to enhance visual customization.
5. **Configurable Defaults**: Allow setting default values (e.g., priority or due date) in a config file for repeated commands.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push changes to your fork.
5. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Uses the [Todoist API](https://developer.todoist.com/) for task management.

## Contact

For questions or suggestions, reach out to the author:

- **Name**: Anshuman Agrawal
- **Email**: asquare567@gmail.com
- **Website**: [asquare.site](https://www.asquare.site)

