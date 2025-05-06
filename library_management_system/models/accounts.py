from library_management_system.models.book import BookItem
from library_management_system.models.enums import AccountStatus, BookStatus, Constants
from library_management_system.models.notify import Notify
from library_management_system.models.transactions import BookLending, Fine
from library_management_system.utils.date_time_utils import DateTimeUtils


class Address:
    def __init__(self, door_no, street, city, state, zip_code):
        self.door_no: str = door_no
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code


class Person:
    def __init__(self, name, email, phone_number, address):
        self.name: str = name
        self.email: str = email
        self.phone_number: str = phone_number
        self.address: Address = address


class Account(Person):
    def __init__(self, name, email, phone_number, address, password):
        super().__init__(name, email, phone_number, address)
        self.account_id: int = 0
        self._password: str = password
        self.account_status: bool = AccountStatus.ACTIVE.value

    def reset_password(self, current_password: str, new_password: str) -> None:
        if self._password != current_password:
            raise ValueError("Current password is incorrect.")
        self._password = new_password
