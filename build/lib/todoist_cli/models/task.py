# models/task.py

class Task:
    def __init__(self, id, content, due_date=None, priority=1):
        self.id = id
        self.content = content
        self.due_date = due_date
        self.priority = priority

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            content=data.get("content"),
            due_date=data.get("due") and data["due"].get("string"),
            priority=data.get("priority", 1)
        )

    def __repr__(self):
        return f"<Task(id={self.id}, content='{self.content}', due_date='{self.due_date}', priority={self.priority})>"
