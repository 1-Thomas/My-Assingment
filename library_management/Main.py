
from book import Book
from member import Member, TeacherMember, StudentMember
from SaveToJson import save_to_json



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



selection = input("Please select one by typing a number ")
 

if selection ==  "1":
    # Takes user input for details of a book and saves it to the library catalogue
    title = input("Please insert the title: ")
    author = input("Please insert the author: ")
    book_new = Book(title, author)
    save_to_json("Library_catalogue.json", book_new.add_book())
    print(f"{title} Added Successfully")

elif selection == "2":
    # Remove a book from the catalogue
    Book.remove_book()

elif selection == "3":
    # Display all books in the catalogue
    print("Here are all the current books")
    data = Book.list_available_books()
    for x in range(len(data)):
        print(f"Title: {data[x]['Title:']}     Author: {data[x]['Author:']}")


elif selection == "4":
    # Adds either a teacher or student member
    print("Add a new member:")
    print("1. Add Student Member")
    print("2. Add Teacher Member")
    type = input(int("Please enter a number to select a member type 1: Student  2: Teacher): "))
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

elif selection == "5":
    # Remove member
    Member.remove_member()

elif selection == "6":
    # Borrow a book
    Member.borrow_book()

elif selection == "7":
    # Display all borrowed books
    print("Here are all the borrowed books")
    data = Member.list_borrowed_books()
    for x in range(len(data)):
        print(f"Name: {data[x]['Name:']}   Book Borrowed: {data[x]['Book Borrowed:']}")

elif selection == "8":
    # Return a book
    Member.return_book()





