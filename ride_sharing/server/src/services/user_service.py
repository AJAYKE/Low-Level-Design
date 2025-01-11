from src.database.databaseObject import DatabaseObject
from src.repositories.user_repository import UserRepository
from src.utils.constants import UserRole


class UserService:
    def __init__(self):
        self.db = DatabaseObject()
        self.user_repository = UserRepository(self.db)

    def create_user(self, data):
        user_name = data["user_name"]
        phone_number = data["phone_number"]
        country = data["country"]
        email = data.get("email", None)

        self.user_repository.create_user(
            user_name, phone_number, country, UserRole.RIDER.value, email
        )
        return {"message": f"user {user_name} created successfully"}

    def block_user(self, user_id):
        self.user_repository.update_user("is_active", 0, user_id)
        return {"message": f"user account with id {user_id} blocked successfully"}
