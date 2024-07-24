# Shethink-assesment

Library Management System
This is a simple Library Management System implemented in Python. It allows you to manage a collection of books and users. You can add or remove books, check out and return books, and manage user information. The system also allows for searching books by title, author, or ISBN.

Features
Add a New Book: Add new books to the library collection.
Remove a Book: Remove books from the library collection using their ISBN.
Display All Available Books: Show all books currently available in the library.
Search for Books: Search books by title, author, or ISBN.
Check Out a Book: Users can check out available books.
Return a Book: Users can return checked-out books.
Add a New User: Add new users to the library system.
Display All Users: Show all users registered in the library system.
Classes
Book
Represents a book in the library.

Attributes:

title: The title of the book.
author: The author of the book.
isbn: The ISBN of the book.
available: Availability status of the book (default is True).


Library Management System
This is a simple Library Management System implemented in Python. It allows you to manage a collection of books and users. You can add or remove books, check out and return books, and manage user information. The system also allows for searching books by title, author, or ISBN.

Features
Add a New Book: Add new books to the library collection.
Remove a Book: Remove books from the library collection using their ISBN.
Display All Available Books: Show all books currently available in the library.
Search for Books: Search books by title, author, or ISBN.
Check Out a Book: Users can check out available books.
Return a Book: Users can return checked-out books.
Add a New User: Add new users to the library system.
Display All Users: Show all users registered in the library system.
Classes
Book
Represents a book in the library.

Attributes:

title: The title of the book.
author: The author of the book.
isbn: The ISBN of the book.
available: Availability status of the book (default is True).
Methods:

__str__: Returns a string representation of the book.
User
Represents a user of the library.

Attributes:

user_id: The ID of the user.
name: The name of the user.
checked_out_books: A list of books checked out by the user.
Methods:

__str__: Returns a string representation of the user.
Library
Represents the library system.

Attributes:

books: A list of books in the library.
users: A list of users in the library system.
Methods:

add_book(book): Adds a book to the library.
remove_book(isbn): Removes a book from the library using its ISBN.
display_books(): Displays all available books in the library.
search_books(search_term, search_type): Searches for books by title, author, or ISBN.
check_out_book(user_id, isbn): Checks out a book for a user.
return_book(user_id, isbn): Returns a book for a user.
add_user(user): Adds a user to the library system.
display_users(): Displays all users in the library system.
Usage
Run the Program:

Execute the script by running python library_management.py.
Main Menu:

The main menu will be displayed with options to manage books and users.
Options:

Add a new book: Follow the prompts to enter the book details.
Remove a book: Enter the ISBN of the book to remove.
Display all available books: View all books currently available in the library.
Search for books: Enter a search term and select search type (title, author, or ISBN).
Check out a book: Enter the user ID and book ISBN to check out a book.
Return a book: Enter the user ID and book ISBN to return a book.
Add a new user: Follow the prompts to enter the user details.
Display all users: View all users registered in the library system.
Exit: Exit the program.
