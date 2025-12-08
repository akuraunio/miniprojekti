import unittest
from bibtex_transform import ReferenceToBibtex
from entities import references
from reference_data import MockReferenceType, MockReferenceField


class TestTransformReferencesToBibtex(unittest.TestCase):
    def setUp(self):
        self.bibtex_exporter = ReferenceToBibtex()

    def test_reference_to_bibtex_returns_correct_string(self):
        ref = references.Reference(
            MockReferenceType.TEST,
            1,
            {
                MockReferenceField.TITLE: "Raamattu",
                MockReferenceField.AUTHOR: "Jeesus",
                MockReferenceField.YEAR: 1,
                MockReferenceField.TEST_TEXTAREA: "",  # testaa että tyhjä arvo jää pois bibtexistä
            },
        )

        # BibTexin viitteen avain on None koska testi reference datassa ei ole KEY kenttää
        self.assertEqual(
            self.bibtex_exporter.reference_to_bibtex(ref),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\n}",
        )

    def test_get_multiple_references_to_bibtex(self):
        ref1 = references.Reference(
            MockReferenceType.TEST,
            1,
            {
                MockReferenceField.TITLE: "Raamattu",
                MockReferenceField.AUTHOR: "Jeesus",
                MockReferenceField.YEAR: 1,
            },
        )

        ref2 = references.Reference(
            MockReferenceType.TEST,
            1,
            {
                MockReferenceField.TITLE: "Aapinen",
                MockReferenceField.AUTHOR: "Mikael Agricola",
                MockReferenceField.YEAR: 1700,
            },
        )

        refs = [ref1, ref2]

        self.assertEqual(
            self.bibtex_exporter.references_to_bibtex(refs),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\n}\n\n@test{None,\ntitle = {Aapinen},\nauthor = {Mikael Agricola},\nyear = {1700},\n}",
        )

    def test_reference_to_bibtex_pages_both_is_correct(self):
        ref = references.Reference(
            MockReferenceType.TEST,
            1,
            {
                MockReferenceField.TITLE: "Raamattu",
                MockReferenceField.AUTHOR: "Jeesus",
                MockReferenceField.YEAR: 1,
                MockReferenceField.PAGES_FROM: 20,
                MockReferenceField.PAGES_TO: 30,
            },
        )

        self.assertEqual(
            self.bibtex_exporter.reference_to_bibtex(ref),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\npages = {20--30},\n}",
        )

    def test_reference_to_bibtex_page_from_only(self):
        ref = references.Reference(
            MockReferenceType.TEST,
            1,
            {
                MockReferenceField.TITLE: "Raamattu",
                MockReferenceField.AUTHOR: "Jeesus",
                MockReferenceField.YEAR: 1,
                MockReferenceField.PAGES_FROM: 20,
            },
        )

        self.assertEqual(
            self.bibtex_exporter.reference_to_bibtex(ref),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\npages = {20},\n}",
        )

    def test_reference_to_bibtex_page_to_only(self):
        ref = references.Reference(
            MockReferenceType.TEST,
            1,
            {
                MockReferenceField.TITLE: "Raamattu",
                MockReferenceField.AUTHOR: "Jeesus",
                MockReferenceField.YEAR: 1,
                MockReferenceField.PAGES_TO: 30,
            },
        )

        self.assertEqual(
            self.bibtex_exporter.reference_to_bibtex(ref),
            "@test{None,\ntitle = {Raamattu},\nauthor = {Jeesus},\nyear = {1},\npages = {30},\n}",
        )
