from sqlalchemy import text
from config import db
from entities.tags import Tag


def tag_from_row(row) -> Tag:
    tag = Tag(
        id=row._mapping["id"],  # pylint: disable=protected-access
        name=row._mapping["name"],  # pylint: disable=protected-access
    )
    return tag


def get_tags() -> list[Tag]:
    result = db.session.execute(text("SELECT * FROM Tag"))
    tags = [tag_from_row(row) for row in result.all()]
    return tags


# haetaan tietokannasta tägi id:n mukaan
def get_tag_by_id(tag_id) -> Tag | None:
    result = db.session.execute(
        text("SELECT * FROM Tag WHERE id = :id"), {"id": tag_id}
    )
    row = result.first()
    if not row:
        return None
    return tag_from_row(row)


# haetaan tietokannasta tägi nimen mukaan
def get_tag_by_name(name: str) -> Tag | None:
    result = db.session.execute(
        text("SELECT * FROM Tag WHERE name = :name"),
        {"name": name},
    )
    row = result.first()
    if not row:
        return None
    return tag_from_row(row)


def add_new_tag(name):
    db.session.execute(text("INSERT INTO Tag (name) VALUES (:name)"), {"name": name})
    db.session.commit()


# tägien muokkaus tietokantaan
def update_tag(tag_id: str, name):
    db.session.execute(
        text("UPDATE Tag SET name = :name WHERE id = :id"), {"name": name, "id": tag_id}
    )
    db.session.commit()


def delete_tag(tag_id: str):
    sql = text("DELETE FROM Tag WHERE id = :id")
    db.session.execute(sql, {"id": tag_id})
    db.session.commit()


def search_tags(query: str) -> list[Tag]:
    search_query = f"%{query}%"
    sql = text("SELECT * FROM Tag WHERE name ILIKE :query")
    result = db.session.execute(sql, {"query": search_query})
    rows = result.fetchall()

    tags = []
    for row in rows:
        tag = tag_from_row(row)
        tags.append(tag)
    return tags
