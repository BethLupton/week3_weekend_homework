from models.book import *

book1 = Book(0, "Remain in Love", "Chris Frantz", "Biography", False)
book2 = Book(1, "The Gift of Fear", "Gavin de Becker", "Psychology", True)
book3 = Book(2, "Where the Crawdads Sing", "Delia Owens", "Mystery", False)

books=[book1,book2,book3]

def add_new_book(book):
    books.append(book)

def get_book(id):
    for book in books:
        if (book.id == id):
            return book
        
def delete_book(index):
    books.remove(get_book(index))