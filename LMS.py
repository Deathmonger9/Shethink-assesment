class Book:
  def __init__(self, title, author, isbn, available=True):
      self.title = title
      self.author = author
      self.isbn = isbn
      self.available = available

  def __str__(self):
      status = 'Available' if self.available else 'Checked out'
      return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

class User:
  def __init__(self, user_id, name):
      self.user_id = user_id
      self.name = name
      self.checked_out_books = []    

  def __str__(self):
      return f"{self.name} (ID: {self.user_id}) - Checked out books: {len(self.checked_out_books)}"

from datetime import datetime

class Library:
  def __init__(self):
      self.books = []
      self.users = []

  def add_book(self, book):
      self.books.append(book)
      print(f"Added book: {book.title}")

  def remove_book(self, isbn):
      self.books = [book for book in self.books if book.isbn != isbn]
      print(f"Removed book with ISBN: {isbn}")

  def display_books(self):
      if not self.books:
          print("No books in the library.")
      for book in self.books:
          print(book)

  def search_books(self, search_term, search_type='title'):
      results = []
      for book in self.books:
          if search_type == 'title' and search_term in book.title:
              results.append(book)
          elif search_type == 'author' and search_term in book.author:
              results.append(book)
          elif search_type == 'isbn' and search_term in book.isb :
              results.append(book)
      return results

  def check_out_book(self, user_id, isbn):
      for book in self.books:
          if book.isbn == isbn and book.available:
              book.available = False
              for user in self.users:
                  if user.user_id == user_id:
                      user.checked_out_books.append(book)
              print(f"User {user_id} checked out book: {book.title}")
              return True
      return False

  def return_book(self, user_id, isbn):
      for book in self.books:
          if book.isbn == isbn and not book.available:
              book.available = True
              for user in self.users:
                  if user.user_id == user_id:
                      user.checked_out_books = [b for b in user.checked_out_books if b.isbn != isbn]
              print(f"User {user_id} returned book: {book.title}")
              return True
      return False

  def add_user(self, user):
      self.users.append(user)
      print(f"Added user: {user.name}")

  def display_users(self):
      if not self.users:
          print("No users in the system.")
      for user in self.users:
          print(user)

def main():
  library = Library()

  while True:
      print("\nLibrary Management System")
      print("1. Add a new book")
      print("2. Remove a book")
      print("3. Display all available books")
      print("4. Search for books")
      print("5. Check out a book")
      print("6. Return a book")
      print("7. Add a new user")
      print("8. Display all users")
      print("9. Exit")
      choice = input("Enter your choice: ")

      try:
          if choice == '1':
              title = input("Enter book title: ")
              author = input("Enter book author: ")
              isbn = input("Enter book ISBN: ")
              library.add_book(Book(title, author, isbn))
              print("Book added successfully.")

          elif choice == '2':
              isbn = input("Enter book ISBN to remove: ")
              library.remove_book(isbn)
              print("Book removed successfully.")

          elif choice == '3':
              library.display_books()

          elif choice == '4':
              search_term = input("Enter search term: ")
              search_type = input("Search by title, author, or ISBN? ").lower()
              results = library.search_books(search_term, search_type)
              if results:
                  for book in results:
                      print(book)
              else:
                  print("No matching books found.")

          elif choice == '5':
              user_id = input("Enter user ID: ")
              isbn = input("Enter book ISBN to check out: ")
              if library.check_out_book(user_id, isbn):
                  print("Book checked out successfully.")
              else:
                  print("Book is not available or not found.")

          elif choice == '6':
              user_id = input("Enter user ID: ")
              isbn = input("Enter book ISBN to return: ")
              if library.return_book(user_id, isbn):
                  print("Book returned successfully.")
              else:
                  print("Book is not checked out or not found.")

          elif choice == '7':
              user_id = input("Enter user ID: ")
              name = input("Enter user name: ")
              library.add_user(User(user_id, name))
              print("User added successfully.")

          elif choice == '8':
              library.display_users()

          elif choice == '9':
              print("Exiting...")
              break

          else:
              print("Invalid choice. Please try again.")
      except Exception as e:
          print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
