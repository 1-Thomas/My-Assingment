'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

def create_instance():
    # Create a new instance of the Book class
    try:
        book = Book("Eloquent Python", "Abdulhameed")
        print("New instance of Book class created")
    except NameError as e:
        print(e)

    # Create a new instance of the Library class
    try:
        pass
    except NameError as e:
        pass

    # Create a new instance of the Member class
    try:
        pass
    except NameError as e:
        pass

    # Create a new instance of the TeacherMember class
    try:
        pass
    except NameError as e:
        pass
    return 



'''
Library Operations
'''

# Add books to the library


# Add member to the library

# List available books in the library

# Borrow a book from the library

# List borrowed books from the library

