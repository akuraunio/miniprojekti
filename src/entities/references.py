class Citation:
    def __init__(self, id, title, authors, year, isbn, publisher, type):
        self.id = id
        self.title = title
        self.authors = authors
        self.year = year
        self.isbn = isbn
        self.publisher = publisher
        self.type = type

    def __rpr__(self):
        return f"Citation(title={self.title}, authors={self.authors}, year={self.year}, isbn={self.isbn}, publisher={self.publisher}, type={self.type})"
