from config import app, db
from repositories.references_repository import add_new_reference
from reference_data import ReferenceType, reference_data

def seed_references():
    example_references = [
        (
            ReferenceType.BOOK,
            {
                "key": "Rämo2025",
                "author": "Satu Rämö",
                "title": "Tinna",
                "publisher": "WSOY",
                "year": "2025",
            },
        ),
        (
            ReferenceType.ARTICLE,
            {
                "key": "Scrum_guide2020",
                "author": "Schwaber, Ken and Sutherland, Jeff",
                "title": "The Scrum Guide",
                "journal": "The Definitive Guide to Scrum: The Rules of the Game",
                "year": "2020",
            },
        ),
        (
            ReferenceType.MASTERSTHESIS,
            {
                "key": "Luoma2025",
                "author": "Luoma, Annika",
                "title": "Putkilokasvit ja lajirunsaus luontotyypeittäin Pallaksen alueella",
                "school": "Helsingin yliopisto",
                "year": "2025",
            },

        ),
        (
            ReferenceType.MISC,
            {
               "key": "python2025",
                "author": "Python Software Foundation",
                "title": "Python Programming Language",
                "url": "https://www.python.org/",
                "year": "2025",
            },
        ),
        (
            ReferenceType.ARTICLE
,
            {
                "key": "Einstein1905",
                "author": "Albert Einstein",
                "title": "Zur Elektrodynamik bewegter Körper",
                "journal": "Annalen der Physik",
                "year": "1905",
            },
        ),
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