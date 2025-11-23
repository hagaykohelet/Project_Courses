import csv


def load_csv(cnx):
    cursor = cnx.cursor()

    with open("data/courses.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cursor.execute("""INSERT INTO courses(
                              institution, city, address, course,
                              district, telephone, email)
                              values
                              (%s, %s, %s, %s, %s, %s, %s);""", row)

    cnx.commit()
    cursor.close()
    return cnx
