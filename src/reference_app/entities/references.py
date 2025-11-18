class Citation:
    def __init__(self, title, author, year, isbn, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.publisher = publisher
    
    def __rpr__(self):
        return f"Citation(title={self.title}, author={self.author}, year={self.year}, isbn={self.isbn}, publisher={self.publisher})"
    
