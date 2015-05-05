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
            student_group INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id))"""

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
        return self.cursor.lastrowid

    def add_course(self, name):
        self.cursor.execute("""INSERT INTO courses(course_name)
                                VALUES(?)""", (name, ))

    def add_students_to_courses(self, student_id, course_id, student_group):
        self.cursor.execute("""INSERT INTO students_to_courses(
                                            student_id,
                                            course_id,
                                        student_group)VALUES(?,?,?)""",
                            (student_id, course_id, student_group))

    def get_course_id(self, course_name):
        course = self.cursor.execute("""SELECT course_id FROM courses
                                WHERE course_name = ?""", (course_name,))
        return course.fetchone()[0]
