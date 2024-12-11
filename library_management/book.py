import json
import os
from SaveToJson import overwrite
class Book:
    """
    A class to represent a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """

    def __init__(self, title, author):
        """
        Constructs all the necessary attributes for the book object.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        """

        self.title = title
        self.author = author


    def add_book(self):
        """
        Adds a book to the library.

        Args:
        - book (Book): The book to be added.
        """
        return{
            "Title:" : self.title,
            "Author:" : self.author
        }
    


    def remove_book():
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.
        """
        with open("Library_catalogue.json", "r")as file:
            data = json.load(file)
        for x in range(len(data)):
            print(f"{data[x]['Title:']} : {data[x]['Author:']}")

        select = input("Please select the book you would like to remove:")

        for i in range(len(data)):
            if data[i]['Title:'] == select:
                del data[i]
                overwrite("library_catalogue.json", data)
                return


    def list_available_books():
        """
        Lists all available books in the library.
        """
        with open("Library_catalogue.json", "r")as file:
            data = json.load(file)
        return data



            


     




    

