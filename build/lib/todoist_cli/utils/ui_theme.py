from rich import print
from rich.console import Console
from rich.table import Table
from todoist_cli.utils.catppuccin_theme import get_theme
from todoist_cli.utils.config import get_selected_theme

console = Console()
selected_theme = get_theme(get_selected_theme())

