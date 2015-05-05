import sqlite3


class CreateHackBulgariaDatabase:

    def __init__(self):
        create_students_table_query = """CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY,
            student_name TEXT,
            student_github TEXT)"""

        create_courses_table_query = """CREATE TABLE IF NOT EXISTS courses(
            course_id INTEGER PRIMARY KEY,
            course_name TEXT)"""

        create_students_to_courses_table_query = """CREATE TABLE IF NOT EXISTS students_to_courses(
            student_id INTEGER,
            course_id INTEGER,
            student_group BOOLEAN,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id))"""
            # 0 - early course, 1 - lately course

        self.database = sqlite3.connect("hackbulgaria_database")
        self.database.row_factory = sqlite3.Row
        self.cursor = self.database.cursor()

        self.cursor.execute(create_students_table_query)
        self.cursor.execute(create_courses_table_query)
        self.cursor.execute(create_students_to_courses_table_query)

    def add_student(self, name, github):
        self.cursor.execute("""INSERT INTO students(student_name,
                                                student_github)
                                VALUES(?,?)""", (name, github))

    def add_course(self, name):
        self.cursor.execute("""INSERT INTO courses(course_name)VALUES(?)""", (name, ))

    def add_student_to_course(self, student_id, course_id, student_group):
        pass
