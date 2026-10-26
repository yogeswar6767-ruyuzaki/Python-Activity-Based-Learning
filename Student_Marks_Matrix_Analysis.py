# program to find Student Marks Matrix Analysis

number_of_students = int(input("Enter the number of students: "))
number_of_subjects = int(input("Enter the number of subjects: "))

marks = []

for i in range(number_of_students):
    student_marks = []

    for j in range(number_of_subjects):
        mark = float(input("Enter a mark: "))
        student_marks.append(mark)

    marks.append(student_marks)

highest_total = 0
best_student = 0

for i in range(len(marks)):
    total = 0

    for j in range(len(marks[i])):
        total = total + marks[i][j]

    print("Student", i + 1, "total:", total)

    if total > highest_total:
        highest_total = total
        best_student = i + 1

print("Highest total:", highest_total)
print("Top student:", best_student)