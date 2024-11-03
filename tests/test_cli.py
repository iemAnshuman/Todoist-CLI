# tests/test_cli.py
import unittest
from unittest.mock import patch
from todoist_cli.client import TodoistClient

class TestTodoistCLI(unittest.TestCase):
    @patch("client.requests.request")
    def test_add_task(self, mock_request):
        # Mock response for add task
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {
            "id": "12345",
            "content": "Test Task"
        }
        client = TodoistClient("fake_api_token")
        task = client.add_task("Test Task", due_string="tomorrow", priority=2)
        self.assertEqual(task["content"], "Test Task")
        self.assertEqual(task["id"], "12345")

    @patch("client.requests.request")
    def test_delete_task(self, mock_request):
        # Mock response for delete task
        mock_request.return_value.status_code = 204
        client = TodoistClient("fake_api_token")
        result = client.delete_task("12345")
        self.assertIsNone(result)

    @patch("client.requests.request")
    def test_list_tasks(self, mock_request):
        # Mock response for list tasks
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = [
            {"id": "12345", "content": "Task 1"},
            {"id": "67890", "content": "Task 2"}
        ]
        client = TodoistClient("fake_api_token")
        tasks = client.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["content"], "Task 1")

if __name__ == "__main__":
    unittest.main()
