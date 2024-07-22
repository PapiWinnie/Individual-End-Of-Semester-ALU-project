
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