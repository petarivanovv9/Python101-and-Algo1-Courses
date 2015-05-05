from create_hackbulgaria_database import CreateHackBulgariaDatabase
import json
import requests

# dekartovo proizvedenie
# SELECT user_name, user_email, post_title FROM Users
# JOIN Posts ON Users.user_id = Posts.author


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

if __name__ == '__main__':
    main()
