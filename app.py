from db.queries import *
from db.load_csv import *
from config import *


def print_menu():
    print("""
    =======menu=======
    1. load CSV into DB
    2. Search records by institution name
    3. Search records by course name
    4. Find most/least common course
    5. Show course count per district
    6. Free SQL query
    7. Exit
    ==================""")


while True:
    print_menu()
    choice = input("Enter a number from menu: ")
    match "choice":
        case "1":
            load_csv(cnx)

        case "2":
            search_records_by_Institution_Name()

        case "3":
            search_records_by_Course_Name()

        case "4":
            find_most_or_least_common_course()

        case "5":
            show_course_count()

        case "6":
            free_sql_query()

        case "7":
            exit()

