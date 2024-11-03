# models/label.py

class Label:
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
        return f"<Label(id={self.id}, name='{self.name}', color='{self.color}')>"
