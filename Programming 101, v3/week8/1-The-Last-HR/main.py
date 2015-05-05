from create_hackbulgaria_database import CreateHackBulgariaDatabase
import json
import requests
import sys

# dekartovo proizvedenie
# SELECT user_name, user_email, post_title FROM Users
# JOIN Posts ON Users.user_id = Posts.author


def list_courses(db):
    courses = db.get_all_courses()

    for course in courses:
        print ("{} - {}".format(course["course_id"], course["course_name"]))


def list_students(db):
    students = db.get_all_students()

    for student in students:
        print (
            "{} - {} - {}".format(student["student_id"], student["student_name"], student["student_github"]))


def list_student_in_courses(db):
    stundet_in_courses = db.get_student_in_courses()

    for item in stundet_in_courses:
        print ("{} - {}".format(item["student_name"], item["course_name"]))


def main():
    hack_bulgaria_api = "https://hackbulgaria.com/api/students/"
    information = requests.get(hack_bulgaria_api).json()

    courses = set()

    db = CreateHackBulgariaDatabase()

    for item in information:
        for course in item["courses"]:
            courses.add(course["name"])

    for name in courses:
        db.add_course(name)

    db.database.commit()

    for item in information:
        if item["github"] == "" or item["github"] == None:
            item["github"] = "None"
        current_student_id = db.add_student(item["name"], item["github"])
        current_courses = item["courses"]

        for course in current_courses:
            current_course_id = db.get_course_id(course["name"])
            current_student_group = course["group"]
            db.add_students_to_courses(
                current_student_id, current_course_id, current_student_group)

    db.database.commit()

    print ("Menu:")
    print ("1. List all students with their GitHub accounts.")
    print ("2. List all courses.")
    print (
        "3. List all students and for each student - list the courses he has been attending.")
    print (
        "4. Find the students that have attented the most courses in Hack Bulgaria.")
    print ("0. Exit.")

    while True:
        user_command = int(input("command: "))

        if user_command == 1:
            list_students(db)
        elif user_command == 2:
            list_courses(db)
        elif user_command == 3:
            # pass
            list_student_in_courses(db)
        elif user_command == 4:
            pass
        elif user_command == 0:
            sys.exit()
        else:
            print ("Invalid command!")


if __name__ == '__main__':
    main()
