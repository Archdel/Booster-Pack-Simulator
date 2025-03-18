import os
import logging
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DatabaseManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.connection.cursor()
            logging.info("Database connected successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Error connecting to the database: {err}")
            self.connection = None

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            logging.info(f"Query executed: {query}")
        except mysql.connector.Error as err:
            logging.error(f"Error executing query: {err}")

    def fetch_all(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            logging.error(f"Error fetching data: {err}")
            return None

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            logging.info("Database connection closed.")
