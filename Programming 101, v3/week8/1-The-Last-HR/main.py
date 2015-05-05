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
    students = []

    db = CreateHackBulgariaDatabase()

    for item in information:
        for course in item["courses"]:
            courses.add(course["name"])

    for name in courses:
        db.add_course(name)
    db.database.commit()

    for item in information:
        current_dict = {}
        current_dict["name"] = item["name"]
        current_dict["github"] = item["github"]

        if current_dict["github"] == "" or current_dict["github"] == None:
            current_dict["github"] = "None"

        students.append(current_dict)

    for student in students:
        db.add_student(student["name"], student["github"])
    db.database.commit()


if __name__ == '__main__':
    main()
