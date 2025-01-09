from ride_sharing.server.src.database.databaseObject import DatabaseObject
from ride_sharing.server.src.utils.constants import UserRole


class UserRepository:
    def __init__(self):
        self.db = DatabaseObject()

    def create_user(self, user_name, phoneNumber, country, user_role, email_id=None):
        query = """insert into users (user_name, phoneNumber, country, email_id, user_role) values (%s, %s,%s,%s,%s)"""
        params = (user_name, phoneNumber, country, email_id, user_role)
        self.db.execute(query=query, params=params)

    def delete_user(self, id):
        query = "delete from users where id=%s"
        params = id
        self.db.execute(query=query, params=params)

    def update_user(self, field, value, id):
        query = f"update table users set {field}=%s where id=%s"
        params = (value, id)
        self.db.execute(query=query, params=params)
