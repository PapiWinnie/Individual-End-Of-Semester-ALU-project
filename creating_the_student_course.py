#Inizialization of attributes for the student course classes

class Course:
    def __init__(self, name, trimester, credits):
        # Initialize the attributes of the Course class
        self.name = name
        self.trimester = trimester
        self.credits = credits
