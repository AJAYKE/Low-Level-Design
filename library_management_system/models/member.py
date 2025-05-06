from library_management_system.models.accounts import Account
from library_management_system.models.book import BookItem
from library_management_system.models.enums import AccountStatus


class Member(Account):
    def __init__(self, name, email, phone_number, address, password):
        super().__init__(name, email, phone_number, address, password)
        self._member_id: int = 0
        self.account_status: bool = AccountStatus.ACTIVE.value
        self.is_librarian: bool = False
        self.is_member: bool = True
        self._date_of_membership: str = None
        self._borrowed_books: dict = {}
        self.__reserved_books: dict = {}

    @property
    def id(self) -> int:
        return self._member_id

    @property
    def borrowed_books(self) -> int:
        return self._borrowed_books

    @property
    def reserved_books(self) -> int:
        return self.__reserved_books

    @borrowed_books.setter
    def borrowed_books(self, book_item: BookItem) -> None:
        if book_item.book_id in self._borrowed_books:
            raise RuntimeError("Book already borrowed by this user")
        self._borrowed_books[book_item.book_id] = book_item

    @reserved_books.setter
    def reserved_books(self, book_item: BookItem) -> None:
        if book_item.book_id in self.__reserved_books:
            raise RuntimeError("Book already reserved by this user")
        self.__reserved_books[book_item.book_id] = book_item
