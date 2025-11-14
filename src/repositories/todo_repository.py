from config import db


def get_citations(citations_id): #muokkaa lähde.id mikä nimi annetaan
    sql = """SELECT c.id, c.title, c.aloitussivu_id
             FROM citations c
             WHERE c.id = :id"""
    return db.query(sql, [citations_id])

def delete(citations_id): #muokkaa lähde.id jos pitää
    sql = "DELETE FROM citations WHERE id = ?"
    db.execute(sql, [citations_id])