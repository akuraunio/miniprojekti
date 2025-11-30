from sqlalchemy import text
from config import db
from entities.references import Reference
from reference_data import reference_data, ReferenceType


# Database-based functions for storing and retrieving references


def reference_from_row(row) -> Reference:
    fields = {}
    for field in reference_data[ReferenceType(row.reference_type)]["fields"]:
        fields[field] = row._mapping[field.value]  # pylint: disable=protected-access

    reference = Reference(
        type=ReferenceType(row.reference_type),
        id=row.id,
        fields=fields,
    )
    return reference


def get_references() -> list[Reference]:
    result = db.session.execute(text("SELECT * FROM Reference"))

    rows = result.all()
    references = []
    for row in rows:
        reference = reference_from_row(row)
        references.append(reference)
    return references


# haetaan tietokannasta viite id:n mukaan
def get_reference(reference_id) -> Reference | None:
    result = db.session.execute(
        text(f"SELECT * FROM Reference WHERE id = {reference_id}")
    )

    row = result.first()

    if not row:
        return None

    return reference_from_row(row)


def add_new_reference(type: ReferenceType, fields: dict):

    field_names = ", ".join([f'"{field.value}"' for field in fields.keys()])
    field_placeholders = ", ".join([f":{field.value}" for field in fields.keys()])

    sql = text(
        f"INSERT INTO Reference (reference_type, {field_names}) "
        f"VALUES (:reference_type, {field_placeholders})"
    )

    parameters = {field.value: value for field, value in fields.items()}
    parameters["reference_type"] = type.value

    db.session.execute(sql, parameters)
    db.session.commit()


# viitteiden muokkaus tietokantaan
def update_reference(reference_id: str, fields: dict):
    set_clauses = ", ".join(
        [f"{field.value} = :{field.value}" for field in fields.keys()]
    )

    sql = text(f"UPDATE Reference SET {set_clauses} WHERE id = :id")

    parameters = {field.value: value for field, value in fields.items()}
    parameters["id"] = reference_id

    db.session.execute(sql, parameters)
    db.session.commit()


def delete_reference(reference_id: str):
    sql = text("DELETE FROM Reference WHERE id = :id")
    db.session.execute(sql, {"id": reference_id})
    db.session.commit()


def search_references(query: str, field: str = None) -> list[Reference]:
    if field and not query:
        from db_helper import search_field_exists

        rows = search_field_exists(field)
    elif field:
        from db_helper import search_by_field

        rows = search_by_field(query, field)
    else:
        from db_helper import search

        rows = search(query)

    references = []
    for row in rows:
        reference = reference_from_row(row)
        references.append(reference)
    return references
