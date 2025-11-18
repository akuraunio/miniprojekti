from config import db
from sqlalchemy import text
from entities.references import Citation

#väliaikanen:
#references = []
#def get_references():
    #return references

#def add_new_reference(title, authors, year, isbn, publisher):
    #references.append({
        #"title": title,
        #"authors": authors,
        #"year": year,
        #"isbn": isbn,
        #"publisher": publisher
    #})


#rakenne kun halutaan tallentaa tietokantaan ja hakea sieltä viitteitä
def get_references():
    result = db.session.execute(text("SELECT id, title, authors, year, isbn, publisher FROM citations"))
    rows = result.all()
    return [Citation(row.id, row.title, row.authors, row.year, row.isbn, row.publisher) for row in rows]

def get_reference(reference_id):
    sql = text("SELECT id, title, authors, year, isbn, publisher FROM citations WHERE id = :id")
    result = db.session.execute(sql, {"id": reference_id})
    row = result.first()
    if not row:
        return None
    return Citation(row.id, row.title, row.authors, row.year, row.isbn, row.publisher)

def add_new_reference(title, authors, year, isbn, publisher):
    sql = text("INSERT INTO citations (title, authors, year, isbn, publisher) "
                   "VALUES (:title, :authors, :year, :isbn, :publisher)")
        
    db.session.execute(sql, {"title": title, "authors": authors, "year": year, "isbn": isbn, "publisher": publisher})
    db.session.commit()

def update_reference(reference_id, title, authors, year, isbn, publisher):
    sql = text("""UPDATE citations SET title = :title,
                                    authors = :authors,
                                    year = :year,
                                    isbn = :isbn,
                                    publisher = :publisher
                                    WHERE id = :id """)

    db.session.execute(sql, {"title": title, "authors": authors, "year": year, "isbn": isbn, "publisher": publisher, "id": reference_id})
    db.session.commit()
