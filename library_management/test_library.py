'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember
from member import Member
from SaveToJson import save_to_json
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
print("2. Remove Book from Libary")
print("3. Show books in Libary")
print("4. Add New Member to Libary")
print("5. Remove Member to Libary")
print("6. Borrow a book")
print("5. Show borrowed books")
# Add books to the library
selection = int(input("Please select one by typing a number"))

if selection ==  1:
    title = input("Please insert the title: ")
    author = input("Please insert the author: ")
    book_new = Book(title, author)
    save_to_json("Library_catalogue.json", book_new.add_book())


    
elif selection == 2:
    Book.remove_book()

elif selection == 3:
    print("Here are all the current books")
    data = Book.list_available_books()
    for x in range(len(data)):
        print(f"{data[x]['Title:']} : {data[x]['Author:']}")



elif selection == 4:
    name = input("Please member name:")
    mnumber = input("Please author title:")
    member_new = Member(name, mnumber)
    member_new.save_member()

elif selection == 5:
    Member.remove_member()

elif selection == 6:
    Member.borrow_book()

elif selection == 7:
    Member.return_book()
        

# Add member to the library

# List available books in the library


# Borrow a book from the library

# List borrowed books from the library

