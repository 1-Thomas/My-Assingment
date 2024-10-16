class Member:
    """
    A class to represent a library member.

    Attributes:
    name : str
        The name of the member.
    borrowed_books : list
        A list of books borrowed by the member.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the member object.

        Parameters:
        name (str): The name of the member.
        """
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Adds a book to the member's borrowed books list.

        Parameters:
        book (Book): The book to be borrowed.
        """
        self.borrowed_books.append(book)

    def return_book(self, book):
        """
        Removes a book from the member's borrowed books list.

        Parameters:
        book (Book): The book to be returned.
        """
        self.borrowed_books.remove(book)


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