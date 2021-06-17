
x = 'y'
while x == 'y':
    class students:
        def __init__(self, name, grade, course):
            self.name = name
            self.grade = grade
            self.course = course
        def display(self):
            if self.course == "1":
                self.course = "Math"
            elif self.course == "2":
                self.course = "Science"
            elif self.course == "3":
                self.course = "History"
            print("Name:", self.name, "Grade:", self.grade, "Course:", self.course)
        
    name = input("Students Name:")
    while len(name) <= 2:
        name = input('Invalid name, try again... ')
    grade = input("Students Grade:")
    while len(grade) <= 1:
        grade = input("Please input a valid number...")
    course = input("Select a course: 1 - Math:, 2 - Science:, 3 - History: ")
    while course not in ["1", "2", "3"]:
        course = input("Please select a valid course number: 1 - Math, 2 - Science, 3 - History")
    s1 = students(name, grade, course)
    s1.display()
    x = input("Another student..? y/n: ")


