from src.database.databaseObject import DatabaseObject


class UserRepository:
    def __init__(self, db: DatabaseObject):
        self.db = db

    def create_user(self, user_name, phoneNumber, country, user_role, email_id=None):
        query = """insert into users (user_name, phone_number, country, email_id, user_role) values (%s, %s,%s,%s,%s)"""
        print("type(user_role)", type(user_role))
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
