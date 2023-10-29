class Book:
    """A class to represent a book in a library"""

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def showTitle(self):
        return self.title

class Borrower:
    """Represents a person that can borrow books"""

    newIdCode = 1  # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.newIdCode
        Borrower.newIdCode += 1  # Updates for the next new borrower ...
        self.booksBorrowed = []

    def showBorrowerDetails(self):
        print(f"Borrower ID: {self.id}")
        print(f"Name: {self.firstname} {self.lastname}")

    def showAllBooks(self):
        if self.booksBorrowed:
            print("Books Borrowed:")
            for book in self.booksBorrowed:
                print(f"Title: {book.showTitle()}")
        else:
            print("No books borrowed.")

    def borrowBook(self, book):
        if book.available:
            self.booksBorrowed.append(book)
            book.available = False
            print(f"{book.showTitle()} has been borrowed by {self.firstname} {self.lastname}.")
        else:
            print(f"{book.showTitle()} is not available for borrowing.")

class Library:
    """A class to represent a lending library"""

    def __init__(self):
        self.books = []
        self.borrowers = []

    def addBook(self, book):
        self.books.append(book)

    def addBorrower(self, borrower):
        self.borrowers.append(borrower)

    def lendBook(self, borrower, book_title):
        for book in self.books:
            if book.title == book_title:
                if book.available:
                    borrower.booksBorrowed.append(book)
                    book.available = False
                    print(f"{book.title} has been borrowed by {borrower.firstname} {borrower.lastname}.")
                else:
                    print(f"{book.title} is not available for borrowing.")
                return
        print(f"{book_title} is not available in the library.")

def main():
    # Create some books ...
    book1 = Book('Kafkas motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)

    # Create some borrowers ...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.addBorrower(bor1)
    library.addBorrower(bor2)
    library.addBorrower(bor3)

    # Make some loans ...
    library.lendBook(bor1, 'Kafkas motorbike')
    bor1.showBorrowerDetails()
    bor1.showAllBooks()
    library.lendBook(bor2, 'History of Bagpipes')
    bor2.showBorrowerDetails()
    bor2.showAllBooks()
    # Try to lend 'History of Bagpipes' again ...
    library.lendBook(bor3, 'History of Bagpipes')

if __name__ == "__main__":
        main()
