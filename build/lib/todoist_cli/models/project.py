# models/project.py

class Project:
    def __init__(self, id, name, color=None):
        self.id = id
        self.name = name
        self.color = color

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            color=data.get("color")
        )

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}', color='{self.color}')>"
