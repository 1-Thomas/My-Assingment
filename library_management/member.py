import json
from SaveToJson import overwrite
from SaveToJson import save_to_json
class Member:
    """
    A class to represent a library member.

    Attributes:
    name : str
        The name of the member.
    borrowed_books : list
        A list of books borrowed by the member.
    """

    def __init__(self, name, mnumber):
        """
        Constructs all the necessary attributes for the member object.

        Parameters:
        name (str): The name of the member.
        """
        self.name = name
        self.borrowed_books = []
        self.mnumber = mnumber

    
    def add_member(self):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """
        return{
            "Name:" : self.name,
            "Member Number" : self.mnumber
        }



def remove_member():
    """
    Removes a member from the library.
    """
    try:
        with open("member_list.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No members are currently available")
        return

    for x in range(len(data)):
        print(f"{data[x]['Name:']} : {data[x]['Member Number']}")

    select = input("Please type the name of the member you would like to remove: ")

    for i in range(len(data)):
        if data[i]['Name:'] == select:
            del data[i]
            print(f"Member '{select}' removed successfully.")
            overwrite("member_list.json", data)
            return
    print("No members under this name.")


        

def borrow_book():
    """
    Adds a book to the member's borrowed books list.

    Parameters:
    book (Book): The book to be borrowed.
    """

    with open("member_list.json", "r") as file:
        data = json.load(file)
        for x in range(len(data)):
            print(f"{data[x]['Name:']} : {data[x]['Member Number']}")

    member_select = input("Please select which member you are")

    for i in range(len(data)):
        if data[i]['Name:'] == member_select:
            member1 = data[i]['Name:']
            break
    print(member1)

    with open("Library_catalogue.json", "r")as file:
        data = json.load(file)
        for x in range(len(data)):
            print(f"{data[x]['Title:']} : {data[x]['Author:']}")

    select = input("Please select the book you would like to borrow:")

    for i in range(len(data)):
        if data[i]['Title:'] == select:
            book1 = data[i]['Title:']
            del data[i]
            overwrite("Library_catalogue.json", data)
            break
    
    print(f"Member {member1} sucessfully borrowed the book {book1}")
        
    data = {    
        "Member" : member1,
        "Book_Borrowed" : book1
    }

    save_to_json("borrowed_list.json", data)

            

           
    

    def return_book():
        """
        Removes a book from the member's borrowed books list.

        Parameters:
        book (Book): The book to be returned.
        """
        ##self.borrowed_books.remove(book)
        sel = input("Please insert your name:")
        with open("borrowed_list.json", "r") as file:
            data = json.load(file)
        for i in range(len(data)):
            if data[i]['Member'] == sel:
                with open("temp_member.json", "w")as file:
                    json.dump(data[i], file, indent = 4)
                print(f"Here are all the books you have borrowed:{data[i]}")
                #sel2 = input("Please insert the book you would like to return")
                break

        #data = "temp_member.json"
        #for i in range(len(data)):
            #if data[i]["Book_Borrowed"] == sel2:
                #print(f"You sucessfully returned {data[i]}")
                #del data[i]
                #break
 


class StudentMember(Member):
    """
    A class to represent a student member, inheriting from Member.

    Attributes:
    student_id : str
        The student ID of the member.
    """

    def __init__(self, name, student_id):
        """
        Constructs all the necessary attributes for the student member object.

        Parameters:
        name (str): The name of the student member.
        student_id (str): The student ID of the member.
        """
        super().__init__(name)
        self.student_id = student_id


class TeacherMember(Member):
    """
    A class to represent a teacher member, inheriting from Member.

    Attributes:
    teacher_id : str
        The teacher ID of the member.
    """

    def __init__(self, name, teacher_id):
        """
        Constructs all the necessary attributes for the teacher member object.

        Parameters:
        name (str): The name of the teacher member.
        teacher_id (str): The teacher ID of the member.
        """
        super().__init__(name)
        self.teacher_id = teacher_id