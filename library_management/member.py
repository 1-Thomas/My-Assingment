import json
from SaveToJson import overwrite
from SaveToJson import save_to_json
class Member:
    """
    A class to represent a library member.

    Attributes:
    name : str
        The name of the member.
    mnumber : str
        The member number.
    member_type : str
        The member type.
    borrowed_books : list
        A list of books borrowed by the member
    """


    def __init__(self, name, mnumber, member_type):
        """
        Initialises a new member object.
        """

        self.name = name
        self.mnumber = mnumber
        self.member_type = member_type
        self.borrowed_books = []
    
    def add_member(self):
        """
        Adds a new member to the library.

        Returns:
        dict: A dictionary with the members's name, number and type.
        """
        return {
            "Name:": self.name,
            "Member Number:": self.mnumber,
            "Member Type:": self.member_type
        }


    def remove_member():
        """
        Removes a member from the library.

        Allows user to insert the name of the member they want to remove.

        Attributes:
        select (str) selection of a member.
        """
        
        try:
            # Reads the JSON file and loads existing members
            with open("member_list.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No members found")
            return
        
        # Show user all members in a formatted structure
        for x in range(len(data)):
            print(f"Name: {data[x]['Name:']}    Member Number: {data[x]['Member Number:']}")
        
        # Prompt user to input the book they want to remove
        select = input("Please type the name of the member you would like to remove: ")

        # Search and remove member
        for i in range(len(data)):
            if data[i]['Name:'] == select:
                del data[i]
                print(f"Member '{select}' removed successfully.")
                overwrite("member_list.json", data)
                return
            else:
                print("Could not find member")


            

    def borrow_book():
        """
        Adds a book to the member's borrowed books list.

        Prompts user to insert a member and a book they want to borrow from the library

        Attributes:
        member_select (str) selection of a member.
        member_select2 (str) selection of a member number.
        select (str) selection of a book.
        select2 (str) selection of an author.
        
        Returns:
        dict: A dictionary with the members's name, number, book borrowed and book author.
        """
        # Loads members from the JSON file and outputs them
        with open("member_list.json", "r") as file:
            data = json.load(file)
            for x in range(len(data)):
                print(f"Name: {data[x]['Name:']}")

        # Users user input to select member name and number
        member_select = input("Please select which member you are ")
        member_select2 = input("Please insert your member number ")
        
        # Validates the user input
        for i in range(len(data)):
            if data[i]['Name:'] == member_select and data[i]['Member Number:'] == member_select2 :
                member1 = data[i]['Name:']
                member2 = data[i]['Member Number:']
                break
        print(member1)


        # Loads the library catalogue JSON file and outputs all books
        with open("Library_catalogue.json", "r")as file:
            data = json.load(file)
            for x in range(len(data)):
                print(f"Title: {data[x]['Title:']}    Author: {data[x]['Author:']}")
        
        # Prompts user to insert the book and author they would like to borrow
        select = input("Please select the book you would like to borrow: ")
        select2 = input("Please select the author of the book you would like to borrow: ")
        
        # Validates the user selected book and removes it if in the catalogue 
        for i in range(len(data)):
            if data[i]['Title:'] == select and data[i]['Author:'] == select2:
                book1 = data[i]['Title:'] 
                author = data[i]['Author:'] 
                del data[i]
                overwrite("Library_catalogue.json", data)
                break
        
        print(f"Member {member_select} sucessfully borrowed the book {select}")
            
        # Add the borrowed book the the borrowed_list.json with members details attached
        data = {    
            "Name:" : member1,
            "Member Number:" : member2,
            "Book Borrowed:" : book1,
            "Author of Book:" : author
        }

        save_to_json("borrowed_list.json", data)

                

            
        

    def return_book():
        """
        Removes a book from the member's borrowed books list.

        Allows user to input a borrowed book to be returned to the library.

        Attributes:
        sel (str) selection of a member.
        sel2 (str) selection of a member number.
        sel3 (str) selection of a book.
        sel4 (str) selection of an author.
        """
        # Load members from JSON file and output them
        with open("member_list.json", "r") as file:
            data = json.load(file)
            for x in range(len(data)):
                print(f"Name: {data[x]['Name:']}")

        # Users user input to select member name and number
        sel = input("Please insert your name: ")
        sel2 = input("Please insert your member number: ")

        with open("borrowed_list.json", "r") as file:
            data = json.load(file)


        # Output all books borrowed by selected member
        for i in range(len(data)):
            if data[i]['Name:'] == sel and data[i]['Member Number:'] == sel2:
                print("Here are all the books you have borrowed")
                print(f"Book:  {data[i]['Book Borrowed:']}   Author:  {data[i]['Author of Book:']} ")
                sel3 = input("Please insert the book you would like to return ")
                sel4 = input("Please insert the author of the book you would like to return ")
                break
            
        # Validate input and update library_catalogue.json
        for i in range(len(data)):
            if data[i]['Name:'] == sel and data[i]['Member Number:'] == sel2 and data[i]['Book Borrowed:'] == sel3 and data[i]['Author of Book:'] == sel4:
                book_to_return = {
                    "Title:": data[i]['Book Borrowed:'],
                    "Author:": data[i]['Author of Book:']
                }
                try:
                    # Add the returned book back to the library catalogue
                    with open("Library_catalogue.json", "r") as file:
                        library_data = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    library_data = []

                library_data.append(book_to_return)
                overwrite("Library_catalogue.json", library_data)

                # Remove the book from the borrowed list
                del data[i]
                overwrite("borrowed_list.json", data)

                print(f"You successfully returned '{sel3}'.")
                return


    def list_borrowed_books():
        """
        Lists all available books in the library.
        """
        with open("borrowed_list.json", "r")as file:
            data = json.load(file)
        return data

        



class StudentMember(Member):

    def __init__(self, name, mnumber, student_id):
        """
        Initialises a new student member.
        
        Attributes:
        - name (str): Name of student.
        - mnumber (str): Member number for the student.
        - member_type (str) The type of member
        - student_id (str): Student number.
        """
        self.name = name
        self.mnumber = mnumber
        self.member_type = "Student"
        self.borrowed_books = []
        self.student_id = student_id

    def add_member(self):
        """
        Adds a student to the library.
        
        Returns:
        dict: A dictionary with the students's name, number, type and book ID.
        """
        return {
            "Name:": self.name,
            "Member Number:": self.mnumber,
            "Member Type:": self.member_type,
            "Student ID:": self.student_id
        }


class TeacherMember(Member):
    def __init__(self, name, mnumber, teacher_id):

        """
        Initialises a new teacher member.
        
        Attributes:
        - name (str): Name of teacher.
        - mnumber (str): Member number for the teacher.
        - member_type (str) The type of member
        - student_id (str): Teacher number.
        """

        self.name = name
        self.mnumber = mnumber
        self.member_type = "Teacher"
        self.borrowed_books = []
        self.teacher_id = teacher_id

    def add_member(self):
        return {
            "Name:": self.name,
            "Member Number:": self.mnumber,
            "Member Type:": self.member_type,
            "Teacher ID:": self.teacher_id
        }