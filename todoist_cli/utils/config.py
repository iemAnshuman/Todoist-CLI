# utils/config.py
import os
from dotenv import load_dotenv, set_key

load_dotenv()
ENV_FILE = ".env"

def get_api_token():
    api_token = os.getenv("TODOIST_API_TOKEN")
    if not api_token:
        raise EnvironmentError("TODOIST_API_TOKEN not set in environment variables.")
    return api_token

def get_selected_theme():
    return os.getenv("TODOIST_THEME", "catppuccin")

def set_selected_theme(theme_name):
    set_key(ENV_FILE, "TODOIST_THEME", theme_name)