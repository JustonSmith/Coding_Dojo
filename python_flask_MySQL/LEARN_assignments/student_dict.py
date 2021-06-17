courses = ['1 - Math, 2 - Science, 3 - History']

students = []

class_size = input("How many students do you have..?")
def student_dict(class_size):
    for i in range(int(class_size)):
        student = {}
        name = input("Students name: ")
        while len(name) <= 2:
            name = input('Invalid name, try again... ')
            student['Name'] = name
            grade = input("please use a number to represent students grade: ")
            student["Grade"] = grade
            course = input("Select a course: 1 - Math, 2 - Science, 3 - History")
        while course not in ["1", "2", "3"]:
            course = input("Select a valid course number: 1 - Math, 2 - Science, 3 - History")
            student["Course"] = course
            students.append(student)
        print(students)
student_dict(class_size)