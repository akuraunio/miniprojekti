class Tag:
    def __init__(
        self,
        id: int,
        name: str,
    ):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Tag(name={self.name}, id={self.id})"
