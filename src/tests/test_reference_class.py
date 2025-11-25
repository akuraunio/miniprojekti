import unittest
from unittest.mock import Mock
from repositories.references_repository import reference_from_row
from entities.references import Reference


class TestReferenceCreation(unittest.TestCase):
    def test_reference_from_row_creates_reference_object(self):
        row = Mock()

        row.reference_type = "test"
        row.id = 100
        row._mapping = {
            "test_text": None,
            "test_text_required": "Jim Highsmith",
            "test_number": None,
            "test_number_required": 3,
            "test_textarea": None,
            "test_textarea_required": 2001,
            "title": None,
            "author": None,
            "year": None,
        }

        ref = reference_from_row(row)

        self.assertIsInstance(ref, Reference)
