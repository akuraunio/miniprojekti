from typing import Dict
from reference_data import ReferenceField


class Reference:
    def __init__(
        self,
        type: str,
        id: int,
        fields: Dict[ReferenceField, str],
    ):
        self.type = type
        self.id = id
        self.fields = fields

    def __repr__(self):
        return f"Reference(type={self.type}, id={self.id}, fields={self.fields})"
