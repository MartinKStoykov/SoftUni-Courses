from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} by {self.author}"
class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title):
        found_book = next(b for b in self.books if b.title == title)
        if found_book:
            return found_book
        return "Book not in this library"


book = Book("Harry Potter", "That woman idk")
library = Library()
library.add_book(book)
print(library.find_book(book.title))