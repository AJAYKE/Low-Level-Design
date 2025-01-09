from abc import ABC

from ride_sharing.server.src.database.databaseObject import DatabaseObject
from ride_sharing.server.src.repositories.user_repository import UserRepository
from ride_sharing.server.src.utils.constants import UserRole

RIDER = 1
DRIVER = 2


class User(ABC):
    def __init__(
        self,
        user_name,
        phone_number,
        country,
        email=None,
        id=None,
    ):
        self.id = id
        self.user_name = user_name
        self.phone_number = phone_number
        self.country = country
        self.email = email
        self.is_blocked = False
        self.data_repository = UserRepository()

    def add_user(self):
        self.data_repository.create_user(
            self.user_name, self.phone_number, self.country, UserRole.RIDER, self.email
        )
        return "User Created"

    def delete_user(self):
        self.data_repository.delete_user(self.id)
        return "User Deleted"

    def block_user(self):
        self.data_repository.update_user("is_active", 0, self.id)
        return "Account Blocked"

    def add_email(self, email_id):
        self.data_repository.update_user("email_id", email_id, self.id)
        self.email = email_id
        return "updated Email Address"


class Driver(User):
    def update_role(self):
        self.data_repository.update_user("user_role", UserRole.DRIVER, self.id)
        return "Now You are Driver"


class Rider(User):
    def book_ride(self):
        pass
