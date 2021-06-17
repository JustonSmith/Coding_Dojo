# students = dict()
# n = int(input("How many students are there...?:"))

# for i in range(n):
#     sname = ("Enter name of student:")
#     marks = []
#     for j in range(3):
#         mark = float(input("Enter the grades:"))
#         marks.append(mark)
#     students[sname] = marks
# print("Created dictionary of students is...", students)




# Definig a class student, which contain 
# name and Roll number and marks of the student

# class Student(object):
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
    
#     def getmarks(self):
#         return self.marks
    
#     def getroll(self):
#         return self.roll
    
#     def __str__(self):
#         return self.name + ' : ' + str(self.getroll()) +'  ::'+  str(self.getmarks())

# # Defining a function for building a Record 
# # which generates list of all the students    
# def Marks(rec, name, roll, marks):
#     rec.append(Students(name, roll, marks))
#     return rec

# # Main Code
# Record = []
# x = 'y'
# while x == 'y':
#     name = input('Enter the name of the student: ')
#     height = input('Enter the roll number: ')
#     roll = input('Marks: ')
#     Record = Marks(Record, name, roll, height)
#     x = input('another student? y/n: ')
    
# # Printing the list of student
# n = 1
# for el in Record:
#     print(n,'. ', el)
#     n = n + 1


# count = int(input("how many students do you have...?:"))

# class students:
#     def __init__(self, name,):
#         self.name = name
#         self.grades = []
#     def enterGrades(self):
#         for i in range(3):
#             g = int(input("Enter the grades of %s in subject %d: "%(self.name, i+1)))
#             self.grades.append(g)
#     def display(self):
#         print(self.name, "score", self.grades)

# name = input("Name of Student:")
# s1 = students(name)
# s1.enterGrades()
# s1.display()


#Student class
# class Student():

# #Details method to get the student marks and name
# def details(self,mark1,mark2,mark3,name):
# self.m1=mark1
# self.m2=mark2
# self.m3=mark3
# self.n=name

# #printing the marks and name
# def _print(self):
# print(“Enter the mark1:”,self.m1)
# print(“Enter the mark2:”,self.m2)
# print(“Enter the mark3:”,self.m3)
# print(“Enter the name:”,self.n)

# #loop method to check whether student is pass or fail
# def loop(self,passmark=40):
# self.pm=passmark
# if(self.m1>=self.pm):
# print( “Pass”)
# else:
# print( “Fail”)

# if(self.m2>=self.pm):
# print( “Pass”)
# else:
# print( “Fail”)

# if(self.m3>=self.pm):
# print( “Pass”)
# else:
# print( “Fail”)

# #Object creation
# s=Student()

# #passing arguments
# s.details(30,40,50,’sathish’)

# #method calling
# s._print()
# s.loop()

# class Student: 
#     # Constructor 
#     def __init__(self, name, rollno, m1, m2): 
#         self.name = name 
#         self.rollno = rollno 
#         self.m1 = m1 
#         self.m2 = m2 

#     # Function to create and append new student    
#     def accept(self, Name, Rollno, marks1, marks2 ): 
#         # use  ' int(input()) ' method to take input from user 
#         ob = Student(Name, Rollno, marks1, marks2 ) 
#         # ls.append(ob) 


        # 


# class students:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         self.marks = []
#         students.count = students.count + 1
        
#     def enterMarks(self):
#         for i in range(3):
#             m = int(input("Enter the marks of %s in %d subject: "%(self.name, i+1)))
#             self.marks.append(m)
            
#     def display(self):
#         print (self.name, "got ", self.marks)

# name = input("Enter the name of Student:")
# s1 = students(name)
# s1.enterMarks()
# s1.display()
# print ("")
# name = input("Enter the name of Student:")
# s2 = students(name)
# s2.enterMarks()
# s2.display()


# Definig a class student, which contain 
# name and Roll number and marks of the student

class Student(object):
    def __init__(self, name, grade, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def getmarks(self):
        return self.marks
    
    def getroll(self):
        return self.roll
    
    def __str__(self):
        return self.name + ' : ' + str(self.getroll()) +'  ::'+  str(self.getmarks())

# Defining a function for building a Record 
# which generates list of all the students    
def Markss(rec, name, roll, marks):
    rec.append(Student(name, roll, marks))
    return rec

# Main Code
Record = []
x = 'y'
while x == 'y':
    name = input('Enter the name of the student: ')
    height = input('Enter the roll number: ')
    roll = input('Marks: ')
    Record = Markss(Record, name, roll, height)
    x = input('another student? y/n: ')
    
# Printing the list of student
n = 1
for el in Record:
    print(n,'. ', el)
    n = n + 1