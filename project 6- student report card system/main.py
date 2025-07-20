# Using OOP(Basic version)

class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no =roll_no
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def calculate_total(self):
        return sum(self.marks.values())
    
    def calculate_percentage(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total()/len(self.marks)
    
    def display_report(self):
        print("\nReport card")
        print(f"Name:{self.name}")
        print(f"Roll No:{self.roll_no}")
        print("\nsubject-wise Marks:")
        for subject,marks in self.marks.items():
            print(f"{subject}:{marks}")
        print(f"\nTotal Marks:{self.calculate_total()}")
        print("Percentage: ",
              round(self.calculate_percentage(),2),"%")
        self.grade()

    def grade(self):
        percentage = self.calculate_percentage()
        print("\nGrade: ", end = " ")
        if percentage >= 90:
            print("A+")
        elif percentage >= 90:
            print("A")
        elif percentage >= 70:
            print("B")
        elif percentage >= 60:
            print("C")
        elif percentage >= 50:
            print("D")
        else:
            print("F")


# Main program 

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

student = student(name,roll_no)

n = int(input("Enter number of subjects: "))
for _ in range(n):
    subject = input("Enter subjects name: ")
    mark = int(input(f"Enter marks for {subject}: "))
    student.add_marks(subject, mark)

student.display_report()
