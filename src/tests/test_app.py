import unittest
from unittest.mock import Mock
from repositories.references_repository import reference_from_row
from entities.references import Reference


class TestReferenceAppValidation(unittest.TestCase):
    def test_reference_from_row(self):
        row = Mock()

        row.reference_type = "book"
        row.id = 100
        row._mapping = {
            "key": "key123",
            "author": "Jim Highsmith",
            "editor": "Mike Beedle",
            "title": "Agile Manifesto",
            "publisher": "Agile Alliance",
            "year": 2001,
            "volume": None,
            "number": None,
            "pages_from": None,
            "pages_to": None,
            "month": None,
            "note": None,
            "annote": None,
            "doi": None,
            "issn": None,
            "isbn": None,
        }

        ref = reference_from_row(row)

        self.assertIsInstance(ref, Reference)
