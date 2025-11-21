from config import db
from sqlalchemy import text
from entities.references import Citation


# Database-based functions for storing and retrieving references
def get_references():
    result = db.session.execute(
        text("SELECT id, title, authors, year, isbn, publisher, type FROM citations")
    )
    rows = result.all()
    return [
        Citation(
            row.id, row.title, row.authors, row.year, row.isbn, row.publisher, row.type
        )
        for row in rows
    ]


# haetaan tietokannasta viite id:n mukaan
def get_reference(reference_id):
    sql = text(
        "SELECT id, title, authors, year, isbn, publisher, type FROM citations WHERE id = :id"
    )
    result = db.session.execute(sql, {"id": reference_id})
    row = result.first()
    if not row:
        return None
    return Citation(
        row.id, row.title, row.authors, row.year, row.isbn, row.publisher, row.type
    )


def add_new_reference(title, authors, year, isbn, publisher, type):
    sql = text(
        "INSERT INTO citations (title, authors, year, isbn, publisher, type) "
        "VALUES (:title, :authors, :year, :isbn, :publisher, :type)"
    )

    db.session.execute(
        sql,
        {
            "title": title,
            "authors": authors,
            "year": year,
            "isbn": isbn,
            "publisher": publisher,
            "type": type,
        },
    )
    db.session.commit()


# viitteiden muokkaus tietokantaan
def update_reference(reference_id, title, authors, year, isbn, publisher):
    sql = text(
        """UPDATE citations SET title = :title,
                                    authors = :authors,
                                    year = :year,
                                    isbn = :isbn,
                                    publisher = :publisher
                                    WHERE id = :id """
    )

    db.session.execute(
        sql,
        {
            "title": title,
            "authors": authors,
            "year": year,
            "isbn": isbn,
            "publisher": publisher,
            "id": reference_id,
        },
    )
    db.session.commit()
