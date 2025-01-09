import os

import mysql.connector
import pyodbc  # type: ignore
from mysql.connector import Error


class DatabaseObject:
    def __init__(self, database="Central"):
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
            raise Exception(f"unable to connect to db due to {str(e)}")

    def fetch_all(self, query, params):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            raise Exception(f"unable to get the data due to {str(e)}")
        finally:
            cursor.close()
            self.conn.close()

    def execute(self, query, params):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
        except Exception as e:
            raise Exception(f"unable to write to db due to {str(e)}")
        finally:
            cursor.close()
            self.conn.close()
