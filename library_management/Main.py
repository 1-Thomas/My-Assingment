'''
    Test Classes and Methods here
'''

from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

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



def test_add_book(self):
    """
    Test adding a book to the library.
    """
    try:
        book = Book("Test Book", "Test Author")
        save_to_json("test_library_catalogue.json", book.add_book())
        print("Test case for adding a book passed")
    except Exception as e:
        print(f"Error in test_add_book: {e}")

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
print("7. Show borrowed books")
print("8. Return a book")
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
    print("Add a new member:")
    print("1. Add Student Member")
    print("2. Add Teacher Member")
    type = int(input("Select member type (1 for Student, 2 for Teacher): "))

    name = input("Please insert the member's name: ")
    mnumber = input("Please insert the member number: ")

    if type == 1:
        student_id = input("Please insert the student ID: ")
        student_member = StudentMember(name, mnumber, student_id)
        save_to_json("member_list.json", student_member.add_member())


    elif type == 2:
        teacher_id = input("Please insert the teacher ID: ")
        teacher_member = TeacherMember(name, mnumber, teacher_id)
        save_to_json("member_list.json", teacher_member.add_member())

    else:
        print("Invalid syntax inserted")

elif selection == 5:
    Member.remove_member()

elif selection == 6:
    Member.borrow_book()

elif selection == 7:
    print("Here are all the borrowed books")
    data = Member.list_borrowed_books()
    for x in range(len(data)):
        print(f"Member: {data[x]['Member']} Book Borrowed: {data[x]['Book Borrowed']}")

elif selection == 8:
    Member.return_book()


else:
    print("Wrong character inserted")
        

# Add member to the library

# List available books in the library


# Borrow a book from the library

# List borrowed books from the library

