import unittest
from bibtex_transform import reference_to_bibtex, references_to_bibtex
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

    def test_get_multiple_references_to_bibtex(self):
        ref1 = references.Reference(
            TestReferenceType.TEST,
            1,
            {
                TestReferenceField.TITLE: "Raamattu",
                TestReferenceField.AUTHOR: "Jeesus",
                TestReferenceField.YEAR: 1,
            },
        )

        ref2 = references.Reference(
            TestReferenceType.TEST,
            1,
            {
                TestReferenceField.TITLE: "Aapinen",
                TestReferenceField.AUTHOR: "Mikael Agricola",
                TestReferenceField.YEAR: 1700,
            },
        )

        refs = [ref1, ref2]

        self.assertEqual(
            references_to_bibtex(refs),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\n}\n\n@test{None,\ntitle = {Aapinen},\nauthor = {Mikael Agricola},\nyear = {1700},\n}",
        )
