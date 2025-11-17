class Citation:
    def __init__(self, id, title, author, year, isbn, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.publisher = publisher
    
    def __repr__(self):
        return f"Citation(title={self.title}, author={self.author}, year={self.year}, isbn={self.isbn}, publisher={self.publisher})"
    
