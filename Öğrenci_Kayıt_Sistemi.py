import random


def separator():
    print("=" * 40)


def confirm(message):
    while True:
        answer = input(message).strip().upper()

        if answer == "Y":
            return True

        elif answer == "N":
            return False

        print("INVALID CHOICE! PLEASE ENTER Y OR N.")


def return_to_menu():
    return confirm("RETURN TO MENU (Y/N): ")


def read_number(message, minimum, maximum):
    while True:
        value = input(message).strip()

        try:
            number = int(value)

        except ValueError:
            print("PLEASE ENTER A WHOLE NUMBER!")
            separator()
            continue

        if minimum <= number <= maximum:
            return number

        print(f"PLEASE ENTER A NUMBER BETWEEN {minimum} AND {maximum}!")
        separator()


def read_name(message):
    while True:
        # Remove extra spaces between words.
        name = " ".join(input(message).split())

        if name and all(part.isalpha() for part in name.split()):
            return name.upper()

        print("INVALID NAME! PLEASE USE LETTERS AND SPACES.")
        separator()


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def show_student(student):
    print("FIRST NAME:", student["first_name"])
    print("LAST NAME:", student["last_name"])
    print("STUDENT ID:", student["id"])

    if student["grade"] is None:
        print("GRADE: NOT ENTERED")

    else:
        print("GRADE:", student["grade"])

    separator()


def menu():
    separator()
    print("STUDENT REGISTRATION SYSTEM".center(40))
    separator()
    print("1 - ADD STUDENT")
    print("2 - LIST STUDENTS")
    print("3 - FIND STUDENT")
    print("4 - DELETE STUDENT")
    print("5 - UPDATE GRADE")
    print("6 - CALCULATE AVERAGE")
    print("7 - HIGHEST-SCORING STUDENTS")
    print("8 - LOWEST-SCORING STUDENTS")
    print("9 - STUDENT RANKINGS")
    separator()
    print("10 - EXIT")
    separator()


students = []

while True:
    menu()

    choice = read_number("SELECT AN OPTION: ", 1, 10)
    separator()

    if choice == 10:
        break

    elif choice == 1:
        if len(students) >= 900:
            print("STUDENT ID CAPACITY REACHED!")
            separator()
            continue

        first_name = read_name("ENTER THE STUDENT'S FIRST NAME: ")
        last_name = read_name("ENTER THE STUDENT'S LAST NAME: ")

        available_ids = []

        for number in range(100, 1000):
            if find_student(number) is None:
                available_ids.append(number)

        student_id = random.choice(available_ids)

        student = {
            "first_name": first_name,
            "last_name": last_name,
            "grade": None,
            "id": student_id
        }

        students.append(student)

        print("STUDENT ADDED SUCCESSFULLY!")
        show_student(student)

    elif not students:
        print("THE STUDENT LIST IS EMPTY!")
        separator()

    elif choice == 2:
        print("STUDENT LIST")
        separator()

        for position, student in enumerate(students, start=1):
            print("LIST NUMBER:", position)
            show_student(student)

    elif choice == 3:
        student_id = read_number(
            "ENTER THE STUDENT ID TO SEARCH FOR: ", 100, 999
        )

        student = find_student(student_id)

        if student is None:
            print("STUDENT NOT FOUND!")
            separator()

        else:
            print("STUDENT FOUND!")
            show_student(student)

    elif choice == 4:
        student_id = read_number(
            "ENTER THE STUDENT ID TO DELETE: ", 100, 999
        )

        student = find_student(student_id)

        if student is None:
            print("STUDENT NOT FOUND!")

        else:
            print("STUDENT TO DELETE:")
            show_student(student)

            if confirm("DELETE THIS STUDENT (Y/N): "):
                students.remove(student)
                print("STUDENT DELETED SUCCESSFULLY!")

            else:
                print("DELETION CANCELLED.")

        separator()

    elif choice == 5:
        student_id = read_number(
            "ENTER THE STUDENT ID TO UPDATE THEIR GRADE: ", 100, 999
        )

        student = find_student(student_id)

        if student is None:
            print("STUDENT NOT FOUND!")

        else:
            show_student(student)

            new_grade = read_number("ENTER THE NEW GRADE: ", 0, 100)
            old_grade = student["grade"]

            student["grade"] = new_grade

            print("GRADE UPDATED SUCCESSFULLY!")

            if old_grade is None:
                print("PREVIOUS GRADE: NOT ENTERED")

            else:
                print("PREVIOUS GRADE:", old_grade)

            print("NEW GRADE:", new_grade)

        separator()

    elif choice in {6, 7, 8, 9}:
        graded_students = []

        for student in students:
            if student["grade"] is not None:
                graded_students.append(student)

        if not graded_students:
            print("NO GRADES HAVE BEEN ENTERED YET!")
            separator()

        elif choice == 6:
            total = 0

            for student in graded_students:
                total += student["grade"]

            average = total / len(graded_students)

            print("CLASS AVERAGE:", round(average, 2))
            print("STUDENTS WITH GRADES:", len(graded_students))
            print(
                "STUDENTS WITHOUT GRADES:",
                len(students) - len(graded_students)
            )
            separator()

        elif choice == 7:
            highest_grade = max(
                student["grade"] for student in graded_students
            )

            print("HIGHEST-SCORING STUDENTS")
            separator()

            for student in graded_students:
                if student["grade"] == highest_grade:
                    show_student(student)

        elif choice == 8:
            lowest_grade = min(
                student["grade"] for student in graded_students
            )

            print("LOWEST-SCORING STUDENTS")
            separator()

            for student in graded_students:
                if student["grade"] == lowest_grade:
                    show_student(student)

        elif choice == 9:
            ranked_students = sorted(
                graded_students,
                key=lambda student: student["grade"],
                reverse=True
            )

            print("STUDENT RANKINGS")
            separator()

            previous_grade = None
            rank = 0

            for position, student in enumerate(ranked_students, start=1):
                if student["grade"] != previous_grade:
                    rank = position

                print("RANK:", rank)
                show_student(student)

                previous_grade = student["grade"]

            ungraded_count = len(students) - len(graded_students)

            if ungraded_count > 0:
                print("STUDENTS WITHOUT GRADES:", ungraded_count)
                print("THESE STUDENTS ARE NOT INCLUDED IN THE RANKINGS.")
                separator()

    if not return_to_menu():
        break

print("CLOSING THE PROGRAM...")
separator()