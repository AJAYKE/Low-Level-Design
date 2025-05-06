from datetime import datetime

from library_management_system.models.enums import Constants, ReservationStatus


class BookReservation:
    def __init__(self, book_id, user_id, reservation_date):
        self.book_id = book_id
        self.user_id = user_id
        self.reservation_date = reservation_date
        self.reservation_status: ReservationStatus = ReservationStatus.CONFIRMED.value

    def __repr__(self):
        return f"BookReservation(book_id={self.book_id}, user_id={self.user_id}, reservation_date={self.reservation_date})"

    def fetch_reservation_details(self):
        return {
            "book_id": self.book_id,
            "user_id": self.user_id,
            "reservation_date": self.reservation_date,
            "reservation_status": self.reservation_status,
        }


class BookLending:
    def __init__(self, book_id, user_id, lending_date):
        self.book_id = book_id
        self.user_id = user_id
        self.lending_date = lending_date
        self.return_date = None

    def __repr__(self):
        return f"BookLending(book_id={self.book_id}, user_id={self.user_id}, lending_date={self.lending_date}, return_date={self.return_date})"

    def fetch_lending_details(self):
        return {
            "book_id": self.book_id,
            "user_id": self.user_id,
            "lending_date": self.lending_date,
            "return_date": self.return_date,
        }

    def lend_book(self):
        pass


class Fine:
    def __init__(self, user_id, book_id, creation_date):
        self.user_id = user_id
        self.book_id = book_id
        self.creation_date = creation_date

    def calculate_fine(self):
        today = datetime.date.today()
        overdue_days = (today - self.creation_date).days
        if overdue_days > Constants.MAX_BORROW_DAYS:
            return overdue_days * Constants.LATE_FEE_PER_DAY

    def initiate_fine_collection_transaction(self):
        return
