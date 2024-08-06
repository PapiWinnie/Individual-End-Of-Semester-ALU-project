#!/usr/bin/python3

class Student:
    def __init__(self, email, names):
        self.email = email  # Student's email address
        self.names = names  # Student's full name
        self.courses_registered = []  # List of courses the student is registered for
        self.GPA = 0.0  # Student's GPA, initially set to 0.0

    def calculate_GPA(self):
        print(f"\nCalculating GPA for {self.names}")
        print(f"Registered Courses: {[course.name for course in self.courses_registered]}")
        print(f"Grades and Credits: {[(course.grade, course.credits) for course in self.courses_registered]}")
        
        total_points = sum(course.grade * course.credits for course in self.courses_registered)
        total_credits = sum(course.credits for course in self.courses_registered)
    
        if total_credits == 0:
            self.GPA = 0.0
        else:
            self.GPA = total_points / total_credits
    
        print(f"The GPA is: {self.GPA:.2f}\n")
        return self.GPA

    def register_for_course(self, course, grade):
        # Set the grade for the course and add it to the student's registered courses
        course.grade = grade
        self.courses_registered.append(course)
        # Debug: Print confirmation of registration
        print(f"Registered {self.names} for {course.name} with grade {course.grade}\n")


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

    def add_student(self):
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        new_student = Student(email, names)
        self.student_list.append(new_student)
        print(f"Student {names} added.\n")

    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = float(input("Enter course credits: "))
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)
        print(f"Course {name} added.\n")

    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade for the course: "))

        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        if student and course:
            student.register_for_course(course, grade)
        else:
            print("Student or course not found. Please check the details and try again.\n")

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda x: x.GPA, reverse=True)

    def search_by_grade(self):
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))
        filtered_students = [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
        return filtered_students

    def generate_transcript(self):
        for student in self.student_list:
            print(f"Student: {student.names}, Email: {student.email}")
            for course in student.courses_registered:
                print(f"Course: {course.name}, Grade: {course.grade}")
            print(f"GPA: {student.GPA:.2f}\n")
