from db.queries import *
from db.load_csv import *
from db.connection import get_connection

cnx = get_connection()


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


class Main:
    while True:
        print_menu()
        choice = input("Enter a number from menu: ")
        match choice:
            case "1":
                load_csv(cnx)

            case "2":
                institution = input("enter an institution do you want search on: ")
                search_records_by_Institution_Name(institution, cnx)

            case "3":
                course = input("enter a course do you want search on: ")
                search_records_by_Course_Name(course, cnx)

            case "4":
                order_choice = input("which order tou want 1.desc 2.asc: ")
                if order_choice == "1":
                    order = "desc"
                else:
                    order = "asc"
                find_most_or_least_common_course(order, cnx)

            case "5":
                show_course_count(cnx)

            case "6":
                query = input("please enter your query: ")
                free_sql_query(query, cnx)

            case "7":
                exit()


Main()
