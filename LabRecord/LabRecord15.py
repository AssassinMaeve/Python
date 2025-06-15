class Employee:
    def __init__(self):
        self.eid = ""
        self.ename = ""
        self.city = ""
        self.designation = ""
        self.bpay = 0
        self.category = ""

    def accept(self):
        self.eid = input("Enter ID: ")
        self.ename = input("Enter Name: ")
        self.city = input("Enter City: ")
        self.designation = input("Enter Designation: ")
        self.bpay = input("Enter Basic Pay: ")
        self.category = input("Enter Category: ")

    def display(self):
        print(f"{self.eid} | {self.ename} | {self.city} | {self.designation} | {self.bpay} | {self.category}")

# Main
n = int(input("Enter number of employees: "))
employees = []

for i in range(n):
    print(f"\nEmployee {i+1}")
    emp = Employee()
    emp.accept()
    employees.append(emp)

print("\nID | Name | City | Designation | Basic Pay | Category")
for emp in employees:
    emp.display()
