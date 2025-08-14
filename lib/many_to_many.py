class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        
        return [c.author for c in self.contracts()]

    def __repr__(self):
        return f"<Book {self.title}>"


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        
        return [c for c in Contract.all if c.author == self]

    def books(self):
        #
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Creates and returns a new Contract object
        return Contract(self, book, date, royalties)

    def total_royalties(self):
       
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        return f"<Author {self.name}>"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
      
    @classmethod
    def contracts_by_date(cls, date):

        return [c for c in cls.all if c.date == date]

    def __repr__(self):
        return f"<Contract {self.author.name} - {self.book.title} ({self.date})>"
    

a1 = Author("John Doe")
b1 = Book("Python 101")
b2 = Book("OOP Deep Dive")

a1.sign_contract(b1, "2025-08-14", 5000)
a1.sign_contract(b2, "2025-08-14", 3000)

print(a1.contracts())        
print(a1.books())            
print(a1.total_royalties())  

print(b1.contracts())        
print(b1.authors())         

print(Contract.contracts_by_date("2025-08-14"))  

