import json
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

    def save_member(self):
        data = self.add_member()
        with open("member_list.json", "a") as file:
            json.dump(data, file, indent = 4)
    
    
    def remove_member():
        """
        Removes a member from the library.

        Args:
        - member (Member): The member to be removed.
        """
        with open("member_list.json", "r")as file:
            data = json.load(file)
        print(data)

        select = input("Please select the member you would like to remove:")

        for i in range(len(data)):
            if data[i]['Name:'] == select:
                del data[i]
                break
        
        with open("member_list.json", "w")as file:
            json.dump(data, file, indent = 4)


        

    def borrow_book():
        """
        Adds a book to the member's borrowed books list.

        Parameters:
        book (Book): The book to be borrowed.
        """
        ##self.borrowed_books.append(book)
        with open("member_list.json", "r") as file:
            data = json.load(file)
        print(data)

        member_select = input("Please select which member you are")

        for i in range(len(data)):
            if data[i]['Name:'] == member_select:
                member1 = data[i]['Name:']
                break
        print(member1)

        with open("Library_catalogue.json", "r")as file:
            data = json.load(file)
        print(data)

        select = input("Please select the book you would like to borrow:")

        for i in range(len(data)):
            if data[i]['Title:'] == select:
                book1 = data[i]['Title:']
                del data[i]
                break
        
        print(f"Member {member1} sucessfully borrowed the book {book1}")
            
        data = {    
            "Member" : member1,
            "Book_Borrowed" : book1
        }

        with open("borrowed_list.json", "a")as file:
            json.dump(data, file , indent = 4)

            

           
    

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
        print(data)
        for i in range(len(data)):
            if data[i]['Member'] == sel:
                mborrow = data[i]
                print(f"Here are all the books you have borrowed:{data[i]}")
                sel2 = input("Please insert the book you would like to return")
                break

        data = mborrow
        for i in range(len(data)):
            if data[i]["Book_Borrowed"] == sel2:
                print(f"You sucessfully returned {data[i]}")
                del data[i]
                break
 


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