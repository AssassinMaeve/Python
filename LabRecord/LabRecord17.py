class Student:
    def __init__(self):
        self.regno = None
        self.name = None
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0
        self.total = 0

    def accept(self):
        self.regno = input("Enter Registration Number: ")
        self.name = input("Enter Name: ")
        self.marks1 = int(input("Enter Marks 1: "))
        self.marks2 = int(input("Enter Marks 2: "))
        self.marks3 = int(input("Enter Marks 3: "))

    def calculate_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3

    def display(self):
        print(f"Registration Number: {self.regno}")
        print(f"Name: {self.name}")
        print(f"Marks 1: {self.marks1}")
        print(f"Marks 2: {self.marks2}")
        print(f"Marks 3: {self.marks3}")
        print(f"Total Marks: {self.total}")

# Direct execution without __name__ check
student = Student()
student.accept()
student.calculate_total()
student.display()