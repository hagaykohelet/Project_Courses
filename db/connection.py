from config import db_config
import mysql.connector

config = db_config()


def get_connection():
    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
