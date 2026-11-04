
students = []

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    try:
        mark = int(input("Enter student mark: "))

        if mark < 0 or mark > 100:
            print("Invalid mark! Enter marks between 0 and 100.")
            return

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    student = {
        "name": name,
        "mark": mark,
        "grade": get_grade(mark)
    }

    students.append(student)
    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n{:<20} {:<10} {:<10}".format("NAME", "MARK", "GRADE"))
    print("-" * 40)

    for student in students:
        print("{:<20} {:<10} {:<10}".format(
            student["name"],
            student["mark"],
            student["grade"]
        ))


def show_statistics():
    if len(students) == 0:
        print("No student records available.")
        return

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\nClass Average:", round(average, 2))
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)


# Main Menu
while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()
        show_statistics()

