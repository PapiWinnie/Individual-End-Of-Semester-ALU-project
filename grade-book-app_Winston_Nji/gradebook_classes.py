# gradebook_classes.py

class Student:
    def __init__(self, email, names):
        self.email = email  # Student's email address
        self.names = names  # Student's full name
        self.courses_registered = []  # List of courses the student is registered for
        self.GPA = 0.0  # Student's GPA, initially set to 0.0

    # Next step will be to calculate the student's GPA based on the course he/she registered
    def calculate_GPA(self):
        # Calculate GPA based on the registered courses
        total_credits = sum(course.credits for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0
        else:
            total_points = sum(course.grade * course.credits for course in self.courses_registered)
            self.GPA = total_points / total_credits

    # Final step for student initialization will be to register the student for a course
    def register_for_course(self, course):
        self.courses_registered.append(course)


class Course:
    def __init__(self, name, trimester, credits, grade=0):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = grade


class GradeBook:
    def __init__(self):
        self.student_list = []  # List of students
        self.course_list = []  # List of courses

    # Asking the users to input the student information 
    def add_student(self):
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        new_student = Student(email, names)
        self.student_list.append(new_student)

    # Asking the user for course information and details
    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = float(input("Enter course credits: "))
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)

    # Function to prompt the user for student and course information
    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")

        # Finding the student by email
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        # Finding the course by name
        if student and course:
            student.register_for_course(course)

    # Calculation student GPA
    def calculate_GPA(self):
        # Iterate through each student's courses_registered list
        for student in self.student_list:
            student.calculate_GPA()

    # Function to calculate the ranking
    def calculate_ranking(self):
        # Sorting the students GPA in terms of descending order
        sorted_students = sorted(self.student_list, key=lambda x: x.GPA, reverse=True)
        return sorted_students

    # Now working on the searching option
    def search_by_grade(self):
        # Asking the user for a grade range
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))
        # Create a new list with students whose GPA falls within the specified range
        filtered_students = [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
        return filtered_students

    # For loop to generate student transcript
    def generate_transcript(self):
        for student in self.student_list:
            print(f"Student: {student.names}, Email: {student.email}")
            for course in student.courses_registered:
                print(f"Course: {course.name}, Grade: {course.grade}")
            print(f"GPA: {student.GPA}")
