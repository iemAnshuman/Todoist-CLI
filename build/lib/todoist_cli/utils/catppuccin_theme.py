# catppuccin_theme.py

THEMES = {
    "catppuccin": {
        "background": "#1E1E2E",
        "text": "#CDD6F4",
        "priority_1": "#F38BA8",
        "priority_2": "#FAB387",
        "priority_3": "#A6E3A1",
        "priority_4": "#89B4FA",
        "highlight": "#CBA6F7",
    },
    "solarized": {
        "background": "#002b36",
        "text": "#839496",
        "priority_1": "#b58900",
        "priority_2": "#cb4b16",
        "priority_3": "#2aa198",
        "priority_4": "#268bd2",
        "highlight": "#6c71c4",
    },
    # Add more themes here
}

def get_theme(theme_name="catppuccin"):
    return THEMES.get(theme_name, THEMES["catppuccin"])  # Default to 'catppuccin'

