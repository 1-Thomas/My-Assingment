import unittest
from unittest.mock import patch, mock_open
import json
from member import Member, TeacherMember, StudentMember
from book import Book
from SaveToJson import save_to_json, overwrite

'''
    Test Classes and Methods here
'''
#Book Operations

class TestMain(unittest.TestCase):
    def test_add_book(self):
        try:
            book = Book("Eloquent Python", "Abdulhameed")
            with patch('builtins.open', new_callable=mock_open):
                save_to_json("Library_catalogue.json", book.add_book())
            print("Add_book Test Passed")
        except NameError as e:
            print(f"Add_book Test Failed {e}")
        return

    def test_remove_book(self):
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Title:": "Eloquent Python", "Author:": "Abdulhameed"}]') as mock_file:
                Book.remove_book()
            print("Book removed successfully")
        except NameError as e:
            print(f"Error occurred while removing book: {e}")
    
    def test_list_available_books(self):
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Title:": "Eloquent Python", "Author:": "Abdulhameed"}]'):
                books = Book.list_available_books()
                self.assertEqual(len(books), 1)
            print("List_available_books Test Passed")
        except NameError as e:
            print("List_available_books Test Failed")    
    

    # Member Operations

    def test_add_student_member(self):
        try:
            student_member = StudentMember("Alice", "001", "S123")
            with patch('builtins.open', new_callable=mock_open) as mock_file:
                save_to_json("member_list.json", student_member.add_member())
            print("Add_student_member Test Passed")
        except NameError as e:
            print("Add_student_member Test Failed")

    def test_add_teacher_member(self):
        try:
            teacher_member = TeacherMember("Bob", "002", "T456")
            with patch('builtins.open', new_callable=mock_open) as mock_file:
                save_to_json("member_list.json", teacher_member.add_member())
            print("Add_teacher_member Test Passed")
        except NameError as e:
            print("Add_teacher_member Test Failed")

    def test_remove_member(self):
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Name:": "Alice", "Member Number:": "001"}]') as mock_file:
                Member.remove_member()
            print("Remove_member Test Passed")
        except NameError as e:
            print("Remove_member Test Failed")

    # Borrowing and Returning Books

    def test_borrow_book(self):
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Name:": "Alice", "Member Number": "001", "Book Borrowed": "a","Author of book": "a"}]') as mock_file:
                Member.borrow_book()
            print("Borrow_book Test Passed")
        except NameError as e:
            print("Borrow_book Test Failed")

    def test_return_book(self):
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Name:": "Alice", "Member Number": "001","Book Borrowed": "a","Author of book": "a"}]') as mock_file:
                Member.return_book()
            print("Return_book Test Passed")
        except NameError as e:
            print("Return_book Test Failed")

    def test_list_borrowed_books(self):
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Member": "Alice", "Book Borrowed": "Eloquent Python"}]'):
                books = Member.list_borrowed_books()
                self.assertEqual(len(books), 1)
            print("List_borrowed_books Test Passed")
        except NameError as e:
            print("List_borrowed_books Test Failed")




if __name__ == '__main__':
    unittest.main()