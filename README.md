# Assessment 1 - Advanced Programming

## Project Overview
This assessment requires you to create a Python application that simulates a simple library management system. The project will involve the use of Object-Oriented Programming (OOP) techniques, classes, and methods. You will also need to document the problem-solving process and provide a clear analysis of your approach.

## Learning Outcomes
By completing this assessment, you will be able to:
- Evaluate Object-Oriented Programming techniques, associated tools, and Application Program Interfaces.
- Analyze and document a complex task utilizing a range of problem-solving skills.

## Project Requirements

- ### Git Repository:
    - Create a GitHub repository for this project.
    - Commit your code regularly to demonstrate the development process.
    - Include a README file that outlines the project, setup instructions, and usage.

- ### Classes and Methods:
    - Create classes to represent the main entities in the library management system (e.g., Library, Book, Member).
    - Each class should have appropriate attributes and methods.
    - Demonstrate the use of inheritance by creating a subclass for different types of library members (e.g., StudentMember, TeacherMember).

- ### Functionality
    - The Library class should manage a collection of books and members.
    - Implement methods to:
        - Add and remove books from the library.
        - Add and remove members from the library.
        - Borrow and return books.
        - List available books.
        - List borrowed books and their borrowers.

- ### Documentation and Analysis:
    - Document the problem-solving process, including:
        - Initial problem analysis.
        - Design decisions and rationale.
        - Challenges faced and solutions implemented.
        - Example usage of the classes and methods.
    - Use docstrings to document the classes and methods.
    - Include test cases to demonstrate the functionality of your code.

- ### Project Structure
Here is a suggested project structure for your library management system:
```
library_management_system/
├── library_management/
│   ├── __init__.py
│   ├── library.py
│   ├── book.py
│   ├── member.py
│   └── test_library.py
├── README.md
└── requirements.txt
```

- ### Detailed Instructions
    #### Step 1: Create the Git Repository
        - Create a new repository on GitHub named library_management_system.
        - Clone the repository to your local machine.
        - Set up a basic directory structure as shown above.

    #### Step 2: Implement the Classes and Methods
        - Library Class (library.py)
        - Book Class (book.py)
        - Member Class and Subclasses (member.py)
        - Test Cases (test_library.py)

    #### Step 3: Documentation and Analysis
        1. README.md:
            - Provide an overview of the project.
            - Include setup instructions and usage examples.
            - Document the classes, methods, and their functionality.
            #### Classes and Methods
                - Library: Manages a collection of books and members.
                    - add_book(book): Adds a book to the library.
                    - remove_book(book): Removes a book from the library.
                    - add_member(member): Adds a member to the library.
                    - remove_member(member): Removes a member from the library.
                    - borrow_book(book, member): Allows a member to borrow a book.
                    - return_book(book, member): Allows a member to return a book.
                    - list_available_books(): Lists all available books in the library.
                    - list_borrowed_books(): Lists all borrowed books and their borrowers.
                - Book: Represents a book with a title and author.
                - Member: Represents a library member with a name and borrowed books.
                - StudentMember and TeacherMember: Subclasses of Member with additional attributes.
        2. Docstrings:
            - Add docstrings to all classes and methods explaining their purpose and usage.

    #### Step 4: Submission
        1. GitHub Repository:
            - Ensure your repository is complete with all necessary files and documentation.
            - Provide a link to your GitHub repository.

        2. README.md:
            - Ensure the README file is comprehensive and clearly explains the project, setup instructions, and usage.

        3. Documentation:
            - Ensure all classes and methods are well-documented with docstrings.
            - Include a detailed analysis of the problem-solving process in the README or a separate documentation file.

        4. Test Cases:
            - Ensure the test cases cover all major functionalities and edge cases.
            - Verify that all tests pass successfully.

### Feedback
- Feedback will be provided through the Modoole.
- Detailed comments on the code, documentation, and overall approach will be given.
