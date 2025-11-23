import mysql.connector
from db.load_csv import load_csv

cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="soldier_courses_db")

