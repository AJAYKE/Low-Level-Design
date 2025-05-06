from typing import Any, Dict

from library_management_system.models.enums import BookFormat, BookStatus, Constants
from library_management_system.models.notify import Notify
from library_management_system.utils.date_time_utils import DateTimeUtils


class Book:
    def __init__(self, book: Dict[str, Any]):
        self._isbn: str = book["isbn"]
        self._title: str = book["title"]
        self._subject: str = book["subject"]
        self._publisher: str = book["publisher"]
        self._language: str = book["language"]
        self._authors: list[str] = book["authors"]
        self._publication_year: int = book["publication_year"]
        self._number_of_pages: int = book["number_of_pages"]


class BookItem(Book):
    def __init__(self, book: Dict[str, Any]):
        super().__init__(book)
        self._book_id: int = book["book_id"]
        self._rack_number: str = book["rack_number"]
        self._reserved_by: set[int] = []
        self._borrowed_by: Dict[int, str] = {}
        self._borrowed_date: str = ""
        self._due_date: str = ""
        self._book_status: BookStatus = BookStatus.AVAILABLE.value
        self._book_format: BookFormat = book["book_format"]
        self._price = book["price"]

    @property
    def book_id(self) -> int:
        return self._book_id

    @property
    def borrowed_by(self) -> Dict[int, str]:
        return self._borrowed_by

    @property
    def reserved_by(self) -> list[int]:
        return self._reserved_by

    @property
    def book_status(self) -> BookStatus:
        return self._book_status

    @borrowed_by.setter
    def borrowed_by(self, user_id: int) -> None:
        if user_id in self._borrowed_by:
            raise RuntimeError("Book already borrowed by this user")
        self._borrowed_by[user_id] = DateTimeUtils.today()
        self._book_status = BookStatus.BORROWED.value
        self._due_date = DateTimeUtils.due_date(Constants.MAX_BORROW_DAYS)

    @reserved_by.setter
    def reserved_by(self, user_id: int) -> None:
        if user_id in self._reserved_by:
            raise RuntimeError("Book already reserved by this user")
        self._reserved_by.append(user_id)

    def return_book(self, user_id: int) -> None:
        if user_id not in self._borrowed_by:
            raise RuntimeError("Book not borrowed by this user")
        self._borrowed_by.pop(user_id)
        self._book_status = BookStatus.AVAILABLE.value
        self._due_date = ""
        if len(self._reserved_by) > 0:
            self._book_status = BookStatus.RESERVED.value
            Notify(
                user_id,
                self.book_id,
                f"Book {self.title} is now available for you to borrow.",
            ).send_notification()
