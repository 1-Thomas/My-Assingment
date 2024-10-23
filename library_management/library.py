import json


class Library:
    """
    Represents a library.

    Attributes:
    - books (list): A list of books in the library.
    - members (list): A list of members in the library.
    """

    def __init__(self):
        """
        Initializes an empty library.
        """
        self.books = []
        self.members = []

    def add_book():
        """
        Adds a book to the library.

        Args:
        - book (Book): The book to be added.
        """
        title = input("Enter Book Title ")
        author = input("Enter Author ")

        toWrite = {
            "Book Title": title,
            "Author": author
            }

        with open("library_catalogue.json", "a") as f:
            json.dump(toWrite, f, indent = 4)
            f.write(",\n")
        

    def remove_book():
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.

        """
        with open("library_catalogue.json", "r") as f:
            data2 = json.load(f)

        remove = input("Please Enter the book you would like to delete")
        if remove in data2:
            del data2[remove]
        with open("library_catalogue.json", 'w')as f:
            json.dump(data2,"library_catalogue.json", indent=4)


   

   
    
        

    def add_member(self, member):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """
        

    def remove_member(self, member):
        """
        Removes a member from the library.

        Args:
        - member (Member): The member to be removed.
        """
        

    def borrow_book(self, book, member):
        """
        Allows a member to borrow a book from the library.

        Args:
        - book (Book): The book to be borrowed.
        - member (Member): The member borrowing the book.
        """
        if book in self.books:
            self.books.remove(book)
            member.borrow_book(book)

    def return_book(self, book, member):
        """
        Allows a member to return a book to the library.

        Args:
        - book (Book): The book to be returned.
        - member (Member): The member returning the book.
        """
        self.books.append(book)
        member.return_book(book)

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

    def list_borrowed_books(self):
        """
        Lists all borrowed books and their borrowers.
        """
        for member in self.members:
            for book in member.borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, Borrower: {member.name}")
