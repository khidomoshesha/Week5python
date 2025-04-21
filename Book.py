class Book:
    def __init__(self, title, author, publication_year):
        """
        Constructor to initialize a Book object.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        """
        Method to display the book's information.
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

# Creating instances (objects) of the Book class
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)

# Accessing attributes and calling the method
print("Book 1:")
book1.display_info()
print("\nBook 2:")
book2.display_info()

# Inheritance layer (creating a more specific type of Book)
class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        """
        Constructor for FictionBook, inheriting from Book.
        """
        super().__init__(title, author, publication_year)
        self.genre = genre

    # Overriding the display_info method to include the genre
    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

print("\nFiction Book:")
fiction_book = FictionBook("To Kill a Mockingbird", "Harper Lee", 1960, "Classic Literature")
fiction_book.display_info()