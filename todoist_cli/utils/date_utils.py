# utils/date_utils.py
from datetime import datetime

def format_date(date_string):
    """
    Convert a date string to a human-readable format.
    """
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return date_string
