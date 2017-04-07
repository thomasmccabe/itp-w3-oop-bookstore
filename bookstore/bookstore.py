class Bookstore(object):
    
    def __init__(self, name):
        self.name = name
        self.books = []

    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)
    
    def search_books(self, title=None, author=None):
        """
        booklist = []
        if title:
            for book in self.books:
                if title.lower() in book.title.lower():
                    booklist.append(book)
        if author:
            for book in self.books:
                if author == book.author:
                    booklist.append(book)
        return booklist
        """
        
        booklist = []
        for book in self.books:
            if (author == book.author) or (title is not None and title.lower() in book.title.lower()):
                booklist.append(book)
        return booklist
            
class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books

class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)
        # (or) self.author.books.append(self)
    