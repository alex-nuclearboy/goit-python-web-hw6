import sqlite3
from random import randint
from faker import Faker
from datetime import datetime

GROUPS = ['PyWeb20-1', 'PyWeb20-2', 'PyWeb20-3']
DISCIPLINES = [
    'Python Core',
    'Python Web Development',
    'Data Science',
    'Design Patterns',
    'Databases and SQL',
    'Artificial Intelligence',
    'Soft skills',
    'IT English'
]

NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20


def initialize_database(db_path, script_path):
    """
    Initializes the database by creating tables according to the SQL script.

    Parameters:
    - db_path: Path to the SQLite database file.
    - script_path: Path to the SQL script file
                   that contains table creation commands.
    """

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Enable foreign key constraints
        cur.execute("PRAGMA foreign_keys = ON;")

        # Read and execute the SQL script to create tables
        with open(script_path, 'r') as sql_file:
            sql_script = sql_file.read()
        cur.executescript(sql_script)

        # Commit the changes and report success
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as error:
        print(f"Error initializing database: {error}")
        # Rollback any changes if something went wrong
        conn.rollback()
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


def generate_data():
    """
    Generates fake data including groups, student names, teacher names,
    disciplines, and dates for grades.
    """

    # Initialize a Faker generator
    fake = Faker()

    fake_groups = GROUPS
    fake_disciplines = DISCIPLINES
    fake_student_first_names = [
        fake.first_name() for _ in range(NUMBER_STUDENTS)]
    fake_student_last_names = [
        fake.unique.last_name() for _ in range(NUMBER_STUDENTS)]
    fake_teacher_first_names = [
        fake.first_name() for _ in range(NUMBER_TEACHERS)]
    fake_teacher_last_names = [
        fake.unique.last_name() for _ in range(NUMBER_TEACHERS)]

    # Generate academic year date range
    today = datetime.now()
    # If we passed June, the academic year starts this year in September
    if today.month > 6:
        start_date = datetime(today.year, 9, 1)
    else:  # Otherwise, the academic year started last September
        start_date = datetime(today.year - 1, 9, 1)

    # The end date is June 30th of the year following the start date
    end_date = datetime(start_date.year + 1, 6, 30)

    fake_dates = [
        fake.date_between(start_date, end_date)
        for _ in range(int(NUMBER_STUDENTS * NUMBER_GRADES))
    ]

    return (fake_groups, fake_student_first_names, fake_student_last_names,
            fake_teacher_first_names, fake_teacher_last_names,
            fake_disciplines, fake_dates)


def prepare_data(
        _groups,
        _student_first_names, _student_last_names,
        _teacher_first_names, _teacher_last_names,
        _disciplines,
        _grades_dates):
    """
    Prepares data for insertion into the database.

    Parameters:
    - _groups: List of group names.
    - _student_first_names: List of student first names.
    - _student_last_names: List of student last names.
    - _teacher_first_names: List of teacher first names.
    - _teacher_last_names: List of teacher last names.
    - _disciplines: List of discipline names.
    - _grades_dates: List of dates for grades.
    """

    pre_groups = [(group,) for group in _groups]
    pre_students = [(first, last, randint(1, len(_groups))) for first, last
                    in zip(_student_first_names, _student_last_names)]
    pre_teachers = [(first, last) for first, last
                    in zip(_teacher_first_names, _teacher_last_names)]
    pre_disciplines = [(discipline, randint(1, len(pre_teachers)))
                       for discipline in _disciplines]
    pre_grades = [(randint(1, len(pre_students)),
                   randint(1, len(pre_disciplines)),
                   randint(1, 5), date) for date in _grades_dates]

    return pre_groups, pre_students, pre_teachers, pre_disciplines, pre_grades


def insert_data(db_path, _groups, _students, _teachers, _disciplines, _grades):
    """
    Inserts generated data into the database.

    Parameters:
    - db_path: Path to the SQLite database file.
    - _groups: Prepared data for group insertion.
    - _students: Prepared data for student insertion.
    - _teachers: Prepared data for teacher insertion.
    - _disciplines: Prepared data for discipline insertion.
    - _grades: Prepared data for grade insertion.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Insert statements for each table
        sql_to_groups = "INSERT INTO groups(group_name) VALUES (?)"

        sql_to_students = (
             "INSERT INTO students(first_name, last_name, group_id) "
             "VALUES (?, ?, ?)"
        )

        sql_to_teachers = (
             "INSERT INTO teachers(first_name, last_name) VALUES (?, ?)"
        )

        sql_to_disciplines = (
             "INSERT INTO disciplines(discipline_name, teacher_id) "
             "VALUES (?, ?)"
        )

        sql_to_grades = (
            "INSERT INTO grades(student_id, discipline_id, grade, grade_date) "
            "VALUES (?, ?, ?, ?)"
        )

        # Execute insert statements
        cur.executemany(sql_to_groups, _groups)
        cur.executemany(sql_to_teachers, _teachers)
        cur.executemany(sql_to_students, _students)
        cur.executemany(sql_to_disciplines, _disciplines)
        cur.executemany(sql_to_grades, _grades)

        # Commit the changes
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as error:
        print("Error inserting data:", error)
        # Rollback any changes if something went wrong
        conn.rollback()
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()


def main():
    # Paths to the database and SQL script
    db_path = 'university_database.db'
    script_path = 'sql_scripts/create_tables.sql'

    # Initialize the database (create tables)
    initialize_database(db_path, script_path)

    # Generate and prepare data
    groups, students, teachers, subjects, grades = prepare_data(
        *(generate_data())
    )

    # Insert data into the database
    insert_data(db_path, groups, students, teachers, subjects, grades)
    print("Tables created and data inserted successfully.")


if __name__ == '__main__':
    main()
