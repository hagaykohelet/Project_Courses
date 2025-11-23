from config import *


def search_records_by_Institution_Name():
    institution = input("choose a word: ")
    cursor.execute("""SELECT id, institution, city, course, district, telephone, email
        FROM courses
    WHERE institution LIKE CONCAT('%', %s, '%')
    LIMIT 50;""", (institution,))
    print(cursor.fetchall())
    cursor.close()
    cnx.close()

def search_records_by_Course_Name():
    course = input("choose a word: ")
    cursor.execute("""SELECT id, institution, city, course, district, telephone, email
            FROM courses
        WHERE institution LIKE CONCAT('%', %s, '%')
        LIMIT 50;""", (course,))
    print(cursor.fetchall())
    cursor.close()
    cnx.close()


def find_most_or_least_common_course():
    order = input("choose the order do you want: ")
    cursor.execute(f"""SELECT course, COUNT(*) AS num
    FROM courses
    GROUP BY course
    ORDER BY num {order}
    LIMIT 1;""")
    print(cursor.fetchall())
    cursor.close()
    cnx.close()


def show_course_count():
    cursor.execute("""SELECT district, COUNT(*) AS num_courses
    FROM courses
    GROUP BY district
    ORDER BY num_courses DESC;""")
    courses = cursor.fetchall()
    print("מחוז  מספר")
    for course in courses:
        print(f"{course[0]} | {course[1]}")
    cursor.close()
    cnx.close()


def free_sql_query():

    query = input("enter your query")
    cursor.execute(query)
    print(cursor.fetchall())
    cursor.close()
    cnx.close()

