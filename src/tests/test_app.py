import unittest
from unittest.mock import Mock
from repositories.references_repository import reference_from_row
from entities.references import Reference


class TestReferenceAppValidation(unitTest.TestCase):
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
        }

        ref = reference_from_row(row)

        self.assertIsInstance(ref, Reference)
