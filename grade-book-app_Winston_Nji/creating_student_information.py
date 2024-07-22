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
