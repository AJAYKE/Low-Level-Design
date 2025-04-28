from datetime import datetime
from typing import Any, Dict


class Book:
    total_books = 0
    total_borrowed_books = 0
    total_reserved_books = 0
    total_available_books = 0

    def __init__(
        self,
        book: Dict[str, Any],
    ):
        self._book_id = book["book_id"]
        self._title = book["title"]
        self._author = book["author"]
        self._isbn = book["isbn"]
        self._genre = book["genre"]
        self._publication_year = book["publication_year"]
        self._rack_number = book["rack_number"]
        self._copies = book["total_copies"]
        self._available_copies = book["available_copies"]
        self._reserved_by = set()
        self._borrowed_by: Dict[int, str] = {}

    @classmethod
    def add_book(cls, book: Dict[str, Any]) -> "Book":
        new_book = cls(book)
        Book.total_books += 1
        Book.total_available_books += book["available_copies"]
        Book.total_borrowed_books += book["total_copies"] - book["available_copies"]
        Book.total_reserved_books += 0
        return new_book

    def add_copies(self, copies: int) -> int:
        self._copies += copies
        self._available_copies += copies
        Book.total_books += copies
        Book.total_available_books += copies
        return self._available_copies

    def remove_copies(self, copies: int) -> int:
        if copies > self._copies:
            raise ValueError("Cannot remove more copies than available")
        if copies > self._available_copies:
            raise ValueError("Cannot remove more copies than available for borrowing")
        self._copies -= copies
        self._available_copies -= copies
        Book.total_books -= copies
        Book.total_available_books -= copies
        return self._available_copies

    def borrow_book(self, user_id: int) -> int:
        if self._available_copies < 1:
            raise ValueError("No copies available")
        if user_id in self._borrowed_by:
            raise RuntimeError("Book already borrowed by this user")
        self._borrowed_by[user_id] = self.get_todays_date()

        if user_id in self._reserved_by:
            self._reserved_by.remove(user_id)

        self._available_copies -= 1

        Book.total_borrowed_books += 1
        Book.total_available_books -= 1

        return self._available_copies

    def return_book(self, user_id: int) -> int:
        if user_id not in self._borrowed_by:
            raise RuntimeError("User has not borrowed this book")
        self._borrowed_by.pop(user_id)
        self._available_copies += 1

        Book.total_borrowed_books -= 1
        Book.total_available_books += 1

        return self._available_copies

    def reserve_book(self, user_id: int) -> None:
        if user_id in self._borrowed_by:
            raise RuntimeError("Book already borrowed by this user")
        if user_id in self._reserved_by:
            raise RuntimeError("Book already reserved by this user")
        if self._available_copies > 0:
            raise RuntimeError("Book is available for borrowing, not reserving")
        if self._available_copies == 0:
            self._reserved_by.add(user_id)

        Book.total_reserved_books += 1

    @property
    def is_available(self):
        return self._available_copies > 0

    @staticmethod
    def get_todays_date() -> str:
        return datetime.now().strftime("%Y-%m-%d")
