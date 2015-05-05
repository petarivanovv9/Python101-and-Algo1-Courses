import sqlite3


class CreateHackBulgariaDatabase:

    def __init__(self):
        create_students_table_query = """CREATE TABLE IF NOT EXISTS Students(
            student_id INTEGER PRIMARY KEY,
            student_name TEXT,
            student_github TEXT)"""

        create_courses_table_query = """CREATE TABLE IF NOT EXISTS Courses(
            course_id INTEGER PRIMARY KEY,
            course_name TEXT)"""

        create_students_to_courses_table_query = """CREATE TABLE IF NOT EXISTS Students_to_Courses(
            student_id INTEGER,
            course_id INTEGER,
            student_group INTEGER,
            FOREIGN KEY(student_id) REFERENCES Students(student_id),
            FOREIGN KEY(course_id) REFERENCES Courses(course_id))"""

        self.database = sqlite3.connect("hackbulgaria_database")
        self.database.row_factory = sqlite3.Row
        self.cursor = self.database.cursor()

        self.cursor.execute(create_students_table_query)
        self.cursor.execute(create_courses_table_query)
        self.cursor.execute(create_students_to_courses_table_query)

    def add_student(self, name, github):
        self.cursor.execute("""INSERT INTO Students(student_name,
                                                student_github)
                                VALUES(?,?)""", (name, github))
        return self.cursor.lastrowid

    def add_course(self, name):
        self.cursor.execute("""INSERT INTO Courses(course_name)
                                VALUES(?)""", (name, ))

    def add_students_to_courses(self, student_id, course_id, student_group):
        self.cursor.execute("""INSERT INTO Students_to_Courses(
                                            student_id,
                                            course_id,
                                        student_group)VALUES(?,?,?)""",
                            (student_id, course_id, student_group))

    def get_course_id(self, course_name):
        course = self.cursor.execute("""SELECT course_id FROM Courses
                                WHERE course_name = ?""", (course_name,))
        return course.fetchone()[0]

    def get_all_courses(self):
        return self.cursor.execute("""SELECT course_id, course_name
                                            FROM Courses""")

    def get_all_students(self):
        return self.cursor.execute("""SELECT student_id,
                                            student_name,
                                            student_github
                                            FROM Students""")

    def get_student_in_courses(self):
        bam = self.cursor.execute("""SELECT student_name, course_id
                                        FROM Students AS S
                                        JOIN Students_to_Courses AS StoC
                ON S.student_id=StoC.student_id""")

        # opa = self.cursor.execute("""SELECT student_name, course_name, course_id
        #     FROM  Students, Courses
        #         JOIN Students_to_Courses AS StoC
        #             ON S.student_id = StoC.student_id
        #         JOIN Courses AS C
        #             ON StoC.course_id = C.course_id
        #         WHERE StoC.course_id = Courses.course_id""")

        boom = self.cursor.execute("""SELECT student_name, course_name
                FROM Students S
                INNER JOIN Students_to_Courses AS StoC
                ON S.student_id = StoC.student_id
                INNER JOIN Courses AS C
                ON StoC.course_id = C.course_id""")

        return boom
