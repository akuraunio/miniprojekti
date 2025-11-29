import unittest
from bibtex_transform import reference_to_bibtex
from entities import references
from reference_data import TestReferenceType, TestReferenceField


class TestTransformReferencesToBibtex(unittest.TestCase):
    def test_reference_to_bibtex_key_pages_from_pages_to(self):
        ref = references.Reference(
            TestReferenceType.TEST,
            1,
            {
                TestReferenceField.TITLE: "Raamattu",
                TestReferenceField.AUTHOR: "Jeesus",
                TestReferenceField.YEAR: 1,
            },
        )

        # BibTexin viitteen avain on None koska testi reference datassa ei ole KEY kenttää
        self.assertEqual(
            reference_to_bibtex(ref),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\n}",
        )
