#!/usr/bin/python3

from gradebook_classes import GradeBook, Student, Course


# Display Menu
def main():
    gradebook = GradeBook()
    
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.add_course()
        elif choice == '3':
            gradebook.register_student_for_course()
        elif choice == '4':
            gradebook.calculate_GPA()
        elif choice == '5':
            ranking = gradebook.calculate_ranking()
            for student in ranking:
                print(f"{student.email} - {student.GPA}")
        elif choice == '6':
            filtered_students = gradebook.search_by_grade()
            for student in filtered_students:
                print(f"{student.email} - {student.GPA}")
        elif choice == '7':
            gradebook.generate_transcript()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to return to the main menu...")

# Run the main program
if __name__ == "__main__":
    main()