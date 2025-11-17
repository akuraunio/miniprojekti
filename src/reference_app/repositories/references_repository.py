#from config import db
from sqlalchemy import text
from entities.references import Citation

#väliaikanen:
references = []
def get_references():
    return references

def add_new_reference(title, authors, year, isbn, publisher):
    references.append({
        "title": title,
        "authors": authors,
        "year": year,
        "isbn": isbn,
        "publisher": publisher
    })





#rakenne kun halutaan tallentaa tietokantaan ja hakea sieltä viitteitä
#def get_references():
    #result = db.session.execute(text("SELECT id, title, authors, year, isbn, publisher FROM citations"))
    #references = result.fetchall()
    #return [Citation(c[0], c[1], c[2], c[3], c[4], c[5]) for c in citations]

#def add_new_reference(title, authors, year, isbn, publisher):
    #sql = text("INSERT INTO citations (title, author, year, isbn, publisher) "
                   #"VALUES (:title, :author, :year, :isbn, :publisher)")
        
    #db.session.execute(sql, {"title": title, "authors": authors, "year": year, "isbn": isbn, "publisher": publisher})
    #db.session.commit()