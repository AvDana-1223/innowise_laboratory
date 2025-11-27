students = []


def main():
    """Asks the user to choose an action and performs it.

    Options are:
        1. Add a new student
        2. Add grades for a student
        3. Generate a full report
        4. Find the top student
        5. Exit program"""

    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        # validation of user choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            add_grades()
        elif choice == 3:
            full_report()
        elif choice == 4:
            calculate_grades()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid input. Enter a number from 1 to 5.")


def find_student(name):
    """Finds the student by name (not case-sensitive) and returns it if it exists.
    Returns None otherwise."""

    # find the student in the list
    for student in students:
        if student["name"].lower() == name.lower():
            return student


def add_student():
    """Asks for student's name.
    If such student is already in the list - prints corresponding message and returns None.
    Otherwise, adds the basic student's dict to the students list."""

    name = input("Enter student's name: ").strip()

    if find_student(name):
        print("The student is already on the list")
        return

    # adding the student to the students list
    students.append({"name": name, "grades": []})


def add_grades():
    """Asks for student's name.
    If such student is not found in the list - prints corresponding message and returns None.
    Otherwise, repeatedly asks the user to enter a grade and adds it to the student's dict.
    The grade is an integer value between 0 and 100 inclusively.
    Once the user inputs 'done' - returns None.
    """

    name = input("Enter student's name: ").strip()

    student = find_student(name)

    # check if the student was not found and return in this case
    if not student:
        print("A student with that name was not found.")
        return

    while True:
        grade = input("Enter your grade (or 'done' to finish) : ").strip()

        if grade.lower() == "done":
            return

        try:
            grade_int = int(grade)
        except ValueError:
            print("Invalid input. Enter a number from 0 to 100, or 'done'.")
            continue

        if 0 <= grade_int <= 100:
            student['grades'].append(grade_int)
        else:
            print("Enter a number from 0 to 100")


def full_report():
    """Prints a report of student's grades.
    For each student outputs their average grade or "N/A" if the student has no grades
    In the end prints overall report: Overall average, Max average, Min average.
    If all the students have no grades - overall report will be "N/A" as well
    If there are no students at all - prints corresponding message and returns None
    """
    print("--- Student Report ---")

    # check if there are no students and return in this case
    if not students:
        print("Students not found")
        return

    count = 0
    len_count = 0

    # Since the range of grades is 0-100 - we will always change min and max if there is at least one student's average
    max_average = -1
    min_average = 101

    for student in students:
        grades = student["grades"]

        student_grades_sum = sum(grades)
        student_grades_count = len(grades)

        count += student_grades_sum
        len_count += student_grades_count

        try:
            average = round(student_grades_sum / student_grades_count, 1)
            print(f"{student["name"]}'s average grade is {average}")

            if average > max_average:
                max_average = average

            if average < min_average:
                min_average = average
        except ZeroDivisionError:
            print(f"{student["name"]}'s average grade is N/A")
            continue

    # If the max_average stayed -1 it means that there are no students with grades, output "N/A" in this case
    if max_average == -1:
        max_average = 'N/A'
        min_average = 'N/A'
        overall_average = 'N/A'
    else:
        overall_average = round(count / len_count, 1)

    print("-" * 10)

    print(f"Max Average: {max_average}")
    print(f"Min Average: {min_average}")
    print(f"Overall Average: {overall_average}")


def calculate_grades():
    """Finds the student with maximal average grade and prints their name.
    If there are no students at all - prints corresponding message and returns None
    If all the students have no grades - prints corresponding message and returns None
    """

    # check if there are no students and return in this case
    if not students:
        print("Students not found")
        return

    # find top performer using max with key being student's average grade.
    # If student has no grades - treat their average as -1
    # This way if at least one student has grades - it will be "max"
    top_performer = max(
        students,
        key=lambda student: sum(student["grades"]) / len(student["grades"]) if len(student["grades"]) != 0 else -1
    )

    # if "max" top performer has no grades it means that all the students have no grades.
    if not top_performer["grades"]:
        print("Not a single student with grades was found.")
        return

    highest_average = round(sum(top_performer["grades"]) / len(top_performer["grades"]), 1)
    print(f"The student with the highest average is {top_performer["name"]} with a grade of {highest_average}")


if __name__ == "__main__":
    main()
