# client.py
import requests
from requests.exceptions import HTTPError

class TodoistClient:
    BASE_URL = "https://api.todoist.com/rest/v2/"

    def __init__(self, api_token):
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def _request(self, endpoint, method="GET", data=None, params=None):
        url = self.BASE_URL + endpoint
        try:
            response = requests.request(method, url, headers=self.headers, json=data, params=params)
            response.raise_for_status()
            if response.content:
                return response.json()
            return None
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def add_task(self, content, due_string=None, priority=1):
        """
        Add a new task to Todoist.
        """
        task_data = {
            "content": content,
            "due_string": due_string,
            "priority": priority
        }
        return self._request("tasks", method="POST", data=task_data)

    def delete_task(self, task_id):
        """
        Delete a task by ID.
        """
        return self._request(f"tasks/{task_id}", method="DELETE")

    def list_tasks(self, filter=None):
        """
        Retrieve all tasks, optionally filtered.
        """
        params = {"filter": filter} if filter else {}
        return self._request("tasks", method="GET", params=params)

    def sync_tasks(self):
        """
        Sync tasks with Todoist (useful if local caching is used).
        """
        # For simplicity, this function just calls list_tasks in this example,
        # but it can be extended to handle local caching if desired.
        return self.list_tasks()
