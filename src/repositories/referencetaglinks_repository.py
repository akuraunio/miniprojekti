from sqlalchemy import text
from repositories.references_repository import reference_from_row
from repositories.tags_repository import tag_from_row
from config import db


def add_new_referencetaglink(reference_id: str, tag_id: str):
    sql = text(
        "INSERT INTO ReferenceTagLink (reference_id, tag_id) VALUES (:reference_id, :tag_id)"
    )
    db.session.execute(sql, {"reference_id": reference_id, "tag_id": tag_id})
    db.session.commit()


def get_referencetaglinks():
    result = db.session.execute(text("SELECT * FROM ReferenceTagLink"))
    referencetaglinks = result.all()
    return referencetaglinks


def get_tags_for_reference(reference_id):
    sql = text(
        """SELECT * FROM Tag t JOIN ReferenceTagLink rtl 
        ON t.id=rtl.tag_id WHERE rtl.reference_id = :reference_id"""
    )
    rows = db.session.execute(sql, {"reference_id": reference_id})

    tags = []
    for row in rows:
        tag = tag_from_row(row)
        tags.append(tag)
    return tags


def get_references_with_tags(tag_ids):
    sql_tag_ids = ",".join([f"'{tag_id}'" for tag_id in tag_ids])
    sql = text(
        f"""SELECT r.* FROM Reference r JOIN ReferenceTagLink rtl ON
          r.id=rtl.reference_id WHERE rtl.tag_id IN ({sql_tag_ids})
          GROUP BY r.id"""
    )
    rows = db.session.execute(sql)

    references = []
    for row in rows:
        reference = reference_from_row(row)
        references.append(reference)
    return references


def delete_referencetaglink(reference_id, tag_id):
    sql = text(
        "DELETE FROM ReferenceTagLink WHERE reference_id=:reference_id AND tag_id=:tag_id"
    )
    db.session.execute(sql, {"reference_id": reference_id, "tag_id": tag_id})
    db.session.commit()
