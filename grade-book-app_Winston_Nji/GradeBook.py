#Initializing the different attributes of student detailes by using a class method

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

#Next step will be to calculate the studenst GPA based on the course he/she registered

    def calculate_GPA(self):
        # Calculate GPA based on the registered courses
        if len(self.courses_registered) == 0:
            self.GPA = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            total_credits = sum(course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits

#Final step for student initizialization will be to Register the student for a course

    def register_for_course(self, course):
         self.courses_registered.append(course)

#Inizialization of attributes for the student course classes

class Course:
    def __init__(self, name, trimester, credits):
        # Initialize the attributes of the Course class
        self.name = name
        self.trimester = trimester
        self.credits = credits




# Initializing the student_list and course_list as empty arrays
class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

 # Asking the users to input the student information 
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        # Creating a new Student object with the provided student information
        new_student = Student(email, names)
        # Appending the new student to the student_list
        self.student_list.append(new_student)

# Asking the user for course information and details
    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = float(input("Enter course credits: "))
        # Creating a new Course object with the provided data
        new_course = Course(name, trimester, credits)
        # Append the new course to the course_list
        self.course_list.append(new_course)


        
# Prompt the user for student and course information
def register_student_for_course(self):
    student_email = input("Enter student email: ")
    course_name = input("Enter course name: ")

#identifying and finding the student and course in the respecive information
    student = None
    for s in self.student_list:
        if s.email == student_email:
            student = s
            break

    course = None
    for c in self.course_list:
        if c.name == course_name:
            course = c
            break

#Incase the student and the course exists, students get registered to the course
    if student and course:
        course_info = {"name": course.name, "credits": course.credits, "grade": float(input("Enter course grade: "))}
        student.register_for_course(course_info)


