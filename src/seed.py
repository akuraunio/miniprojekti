from config import app, db
from repositories.references_repository import add_new_reference
from reference_data import ReferenceType, reference_data

def seed_references():
    example_references = [

    ]

    for reference_type, fields in example_references:
        full_fields = {}
        for field in reference_data[reference_type]["fields"]:
            key = field.value
            full_fields[field] = fields.get(key)

        add_new_reference(reference_type, full_fields)

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_references()