from library_management_system.models.accounts import Account
from library_management_system.models.book import BookItem
from library_management_system.models.enums import AccountStatus, BookStatus
from library_management_system.models.member import Member
from library_management_system.models.transactions import (
    BookLending,
    BookReservation,
    Fine,
)
from library_management_system.utils.date_time_utils import DateTimeUtils


class Librarian(Account):
    def __init__(self, name, email, phone_number, address, password):
        super().__init__(name, email, phone_number, address, password)
        self.librarian_id: int = 0
        self.account_status: bool = AccountStatus.ACTIVE.value
        self.is_librarian: bool = True
        self.is_member: bool = False
        self._members: dict = {}
        self._books: dict = {}
        self._book_items: dict = {}
        self._borrowed_books: dict = {}
        self._reserved_books: dict = {}

    def add_book(self, book):
        # Logic to add a book to the library
        pass

    def remove_book(self, book_id):
        # Logic to remove a book from the library
        pass

    def add_member(self, member):
        # Logic to add a member to the library
        pass

    def block_member(self, member_id):
        # Logic to block a member
        pass

    def unblock_member(self, member_id):
        # Logic to unblock a member
        pass

    def checkout_book(self, book_item: BookItem, user_id: int) -> None:
        member = self.get_user_by_id(user_id)
        if book_item.book_status != BookStatus.AVAILABLE.value:
            raise RuntimeError("Book is not available for checkout")

        if member.id in book_item.borrowed_by:
            raise RuntimeError("Book already borrowed by this user")

        if book_item.reserved_by and self._member_id not in book_item.reserved_by:
            raise RuntimeError("Book is reserved by another user")

        if len(member.borrowed_books) >= 5:
            raise RuntimeError("Borrow limit reached")

        member.borrowed_books(book_item)
        lending = BookLending(book_item.book_id, self._member_id, DateTimeUtils.today())
        book_item.borrowed_by(self._member_id)
        self._borrowed_books[book_item.book_id] = lending

    def return_book(self, book_item: BookItem, user_id: int) -> None:
        member = self.get_user_by_id(user_id)
        if book_item.book_status != BookStatus.BORROWED.value:
            raise RuntimeError("Book is not borrowed")

        if member.id not in book_item.borrowed_by:
            raise RuntimeError("Book not borrowed by this user")

        lending_details = self.__fetch_lending_details(book_item)
        if not lending_details:
            raise RuntimeError("No lending details found for this book")

        fine = Fine(user_id, book_item.book_id, lending_details.lending_date)
        fine_amount = fine.calculate_fine()

        if fine_amount:
            fine.initiate_fine_collection_transaction()

        book_item.return_book(user_id)
        member.borrowed_books.pop(book_item.book_id, None)
        self._borrowed_books.pop(book_item.book_id, None)

    def reserve_book(self, book_item: BookItem, user_id: int) -> None:
        member = self.get_user_by_id(user_id)

        if book_item.book_id in member.reserved_books:
            raise RuntimeError("Book already reserved by this user")

        if len(member.reserved_books) >= 5:
            raise RuntimeError("Reservation limit reached")

        reserve = BookReservation(book_item.book_id, user_id, DateTimeUtils.today())
        book_item.reserved_by(user_id)
        member.reserved_books[book_item.book_id] = book_item
        self._reserved_books[book_item.book_id] = reserve

    def __fetch_lending_details(self, book_item: BookItem) -> BookLending:
        return self._borrowed_books.get(book_item.book_id, None)

    @staticmethod
    def get_user_by_id(self, user_id: int) -> Member:
        return self._members.get(user_id, None)
