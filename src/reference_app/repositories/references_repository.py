from config import db
from sqlalchemy import text
from entities.references import Citation

# Database-based functions for storing and retrieving references
def get_references():
    result = db.session.execute(text("SELECT id, title, authors, year, isbn, publisher FROM citations"))
    rows = result.all()
    return [Citation(row.id, row.title, row.authors, row.year, row.isbn, row.publisher) for row in rows]

def add_new_reference(title, authors, year, isbn, publisher):
    sql = text("INSERT INTO citations (title, authors, year, isbn, publisher) "
                   "VALUES (:title, :authors, :year, :isbn, :publisher)")
        
    db.session.execute(sql, {"title": title, "authors": authors, "year": year, "isbn": isbn, "publisher": publisher})
    db.session.commit()
