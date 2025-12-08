import unittest
from unittest.mock import Mock
from repositories.references_repository import reference_from_row
from entities.references import Reference


class TestReferenceCreation(unittest.TestCase):
    def setUp(self):
        self.row = Mock()

        self.row.reference_type = "test"
        self.row.id = 100
        self.row._mapping = {
            "key": "testiviite1",
            "test_text": None,
            "test_text_required": "Jim Highsmith",
            "test_number": None,
            "test_number_required": 3,
            "test_textarea": None,
            "test_textarea_required": 2001,
            "title": None,
            "author": None,
            "year": None,
            "pages_from": None,
            "pages_to": None,
        }

    def test_reference_from_row_creates_reference_object(self):
        ref = reference_from_row(self.row)

        self.assertIsInstance(ref, Reference)

    def test_reference_repr(self):
        ref = reference_from_row(self.row)
        repr_actual = repr(ref)

        # testaa että repr palauttaa oikean viite tyypin ja id:n
        self.assertIn("MockReferenceType.TEST", repr_actual)
        self.assertIn("id=100", repr_actual)
