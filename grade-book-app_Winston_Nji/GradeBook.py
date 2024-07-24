# Initializing the different attributes of student details by using a class method

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

# Initialization of attributes for the student course classes

class Course:
    def __init__(self, name, trimester, credits, grade=0):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = grade
# Initializing the student_list and course_list as empty arrays
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
        for i in range(len(self.student_list) - 1):
            for j in range(len(self.student_list) - 1 - i):
                if self.student_list[j].GPA < self.student_list[j + 1].GPA:
                    # Swapping the students if the current student's GPA is less than the next student's GPA
                    temp = self.student_list[j]
                    self.student_list[j] = self.student_list[j + 1]
                    self.student_list[j + 1] = temp

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
            print(f"Student: {student.names} - Email: {student.email}")
            print("Courses Registered:")
            for course in student.courses_registered:
                print(f"  Course: {course['name']} - Credits: {course['credits']} - Grade: {course['grade']}")
            print(f"GPA: {student.GPA}")
            print("")

# Display Menu
def main():
    gradebook = GradeBook()

    while True:
        print("Menu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            gradebook.add_student()
        elif choice == "2":
            gradebook.add_course()
        elif choice == "3":
            gradebook.register_student_for_course()
        elif choice == "4":
            gradebook.calculate_GPA()
        elif choice == "5":
            gradebook.calculate_ranking()
        elif choice == "6":
            filtered_students = gradebook.search_by_grade()
            for student in filtered_students:
                print(f"Student: {student.names} - GPA: {student.GPA}")
        elif choice == "7":
            gradebook.generate_transcript()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()