'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

def create_instance(self, book_new):
    # Create a new instance of the Book class
    
    try:
        book_new = Book("Eloquent Python", "Abdulhameed")
        print("New instance of Book class created")
        pass
    except NameError as e:
         print(e)

    # Create a new instance of the Library class
    try:
        pass
    except NameError as e:
        pass

    # Create a new instance of the Member class
    try:
        member = Member("Thomas", 3)
        print("New instance of Member class created")
        pass
    except NameError as e:
        print(e)
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


print("Welcome to our Libary! Please choose on option:")
print("1. Add Book to Libary")
print("2. Add New Member to Libary")
print("3. Show books in Libary")
print("4. Borrow a book")
print("5. Show borrowed books")
# Add books to the library
selection = int(input("Please select one by typing a number"))

if selection ==  1:
    title = input("Please insert title:")
    author = input("Please author title:")
    book_new = Book(title, author)
    book_new.save_book()
    
    

elif selection == 2:
    Book.remove_book()    

# Add member to the library

# List available books in the library


# Borrow a book from the library

# List borrowed books from the library

