# utils/config.py
import os

def get_api_token():
    api_token = os.getenv("TODOIST_API_TOKEN")
    if not api_token:
        raise EnvironmentError("TODOIST_API_TOKEN not set in environment variables.")
    return api_token
