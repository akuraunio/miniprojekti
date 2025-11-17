class Citation:
    def __init__(self, title, authors, year, isbn, publisher):
        self.title = title
        self.authors = authors
        self.year = year
        self.isbn = isbn
        self.publisher = publisher
    
    def __rpr__(self):
        return f"Citation(title={self.title}, authors={self.authors}, year={self.year}, isbn={self.isbn}, publisher={self.publisher})"
    
