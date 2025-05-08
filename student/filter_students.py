import stdio
from student import Student

def main():
    students = []

    while not stdio.isEmpty():
        name = stdio.readString()
        major = stdio.readString()
        grade = stdio.readFloat()

        new_student = Student(name, major)

        for student in students:
            if student == new_student:
                student.addGrade(grade)
                break
            else:
                new_student.addGrade(grade)
                students.append(new_student)

        for student in students:
            print(str(student))

        if students:
            top_student = max(students, key=lambda s: s.getGPA())
            print(f"Top student: {top_student}")

if __name__ == '__main__':
    main()
