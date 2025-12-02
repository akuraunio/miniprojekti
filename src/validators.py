from flask import abort
from reference_data import (
    ReferenceFieldType, 
    TestReferenceType,
    reference_fields,
    reference_data,
    test_reference_data,
    test_reference_fields
)

# validointien apufunktiot
def _validate_required(field_name, field_value, required):
    if required and not field_value:
        abort(400, f"Täytä kaikki pakolliset kentät: {field_name}")

def _validate_number(field_name, field_value):
    value = str(field_value).strip()
    if not value.lstrip("-").isdigit():
        abort(400,f"{field_name} täytyy olla numero")

    if int(value) < 0:
        abort(400, "Vuosi ei voi olla negatiivinen")

def _validate_text(field_value, field_name):
    if not any(char.isalnum()for char in field_value):
        abort(400,f"{field_name} ei voi sisältää vain erikoismerkkejä")

def _validate_single_field(field_name, field_type, field_value):
    if field_type == ReferenceFieldType.NUMBER:
        _validate_number(field_name, field_value)

    if field_type in (ReferenceFieldType.TEXT, ReferenceFieldType.TEXTAREA):
        _validate_text(field_value, field_name)

# viitteiden kenttien validointi
def _validate_required_fields(reference_type, form):
    if isinstance(reference_type, TestReferenceType):
        data_dict = test_reference_data
        fields_dict = test_reference_fields
    else:
        data_dict = reference_data
        fields_dict = reference_fields
  
    for field, meta in data_dict[reference_type]["fields"].items():
        field_value = form.get(field.value)

        if not field_value and not meta["required"]:
            continue

        field_name = fields_dict[field]["name"]
        field_type = fields_dict[field]["type"]

        _validate_required(field_name, field_value, meta["required"])

        if not field_value:
            continue

        _validate_single_field(field_name, field_type, field_value)
