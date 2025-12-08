import unittest
from werkzeug import exceptions
from ref_app import _validate_required_fields
from reference_data import MockReferenceType


class TestUserInputFormValidation(unittest.TestCase):
    def test_validate_required_fields_is_passed_with_correct_input(self):
        ref_type = MockReferenceType.TEST
        form_input = {
            "key": "testikey1",
            "test_text_required": "teksti",
            "test_number_required": 3,
            "test_textarea_required": "tekstikenttä",
        }

        _validate_required_fields(ref_type, form_input)

    def test_validate_required_fields_aborts_with_incomplete_input(self):
        ref_type = MockReferenceType.TEST
        form_input = {}

        with self.assertRaises(exceptions.BadRequest):
            _validate_required_fields(ref_type, form_input)
