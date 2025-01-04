import unittest
from unittest.mock import patch, mock_open
import json
from member import Member, TeacherMember, StudentMember
from book import Book
from SaveToJson import save_to_json, overwrite

'''
    Test Classes and Methods 
'''
#Book Operations

class TestMain(unittest.TestCase):
    def test_return_book(self):
        """
        Test case for returning a book.
        
        Mocks the Member.return_book() function using sample data to test if a member return a book.
        """
        try:
            with patch('builtins.open', new_callable=mock_open, read_data='[{"Name:": "Alice", "Member Number:": "2","Book Borrowed:": "a", "Author of Book:": "a"}]') as mock_file:
                Member.return_book()
            print("Return_book Test Passed")
        except NameError as e:
            print("Return_book Test Failed")



if __name__ == '__main__':
    unittest.main()