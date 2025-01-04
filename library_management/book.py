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

        Attributes:
        title (str): The title of the book.
        author (str): The author of the book.

        Returns:
        dict: A dictionary with the book's title and author.
        """
        return{
            "Title:" : self.title,
            "Author:" : self.author
        }
    


    def remove_book():
        """
        Removes a book from the library.

        Attributes:
        select (str) selection of a book.
        """

        with open("Library_catalogue.json", "r") as file:
            data = json.load(file)

        # Shows user all books
        for x in range(len(data)):
            print(f"Title: {data[x]['Title:']}    Author: {data[x]['Author:']}")
        
        # Prompts user to input the book they want to remove
        select = input("Please select the book you would like to remove: ")
       
        # Search and remove the book
        for i in range(len(data)):
            if data[i]['Title:'] == select:
                del data[i]
                overwrite("library_catalogue.json", data)
                print(f"{select} Deleted Successfully")
                return





    def list_available_books():
        """
        Lists all available books in the library.

        """

        with open("Library_catalogue.json", "r")as file:
            data = json.load(file)
        return data
