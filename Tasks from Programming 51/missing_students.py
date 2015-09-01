def main():
    students = []

    number_students = int(input())

    while number_students > 0:
        student = input()
        students.append(student)
        number_students -= 1

    number_days = int(input())
    all_missing_students = []

    while number_days > 0:
        curr_num_students = int(input())
        curr_students = []

        while curr_num_students > 0:
            curr_student = input()
            curr_students.append(curr_student)
            curr_num_students -= 1

        curr_missing = []
        for i in students:
            if i not in curr_students:
                curr_missing.append(i)

        all_missing_students.append(curr_missing)

        number_days -= 1

    print(all_missing_students)


if __name__ == '__main__':
    main()
