def cli():
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
    choice = input("Enter a number from menu: ")
    return choice
