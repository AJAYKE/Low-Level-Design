import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()


class DatabaseObject:
    def __init__(self, database="RIDESHARING"):
        self.user_name = os.environ.get("DATABASE_USERNAME")
        self.password = os.environ.get("DATABASE_PASSWORD")
        self.server = os.environ.get("DATABASE_SERVER")
        self.database = database
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                user=self.user_name,
                password=self.password,
                port=3306,
                database=self.database,
            )
        except Error as e:
            raise Exception(f"Unable to connect to DB due to {str(e)}")

    def fetch_all(self, query, params=None):
        cursor = None
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(query, params)
            raise Exception(f"Unable to fetch data due to {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()

    def execute(self, query, params=None):
        cursor = None
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(query, params)
            raise Exception(f"Unable to execute query due to {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()


if __name__ == "__main__":
    db = DatabaseObject()
    try:
        db.connect()
        print("Database connection successful!")
    except Exception as e:
        print(f"Failed to connect: {e}")
