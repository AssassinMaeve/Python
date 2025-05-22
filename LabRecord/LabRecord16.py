class Employee:
    def __init__(self):
        self.eid = None
        self.ename = None
        self.city = None
        self.bpay = 0.0
        self.gross_salary = 0.0

    def input_data(self):
        self.eid = input("Enter Employee ID: ")
        self.ename = input("Enter Employee Name: ")
        self.city = input("Enter City: ")
        self.bpay = float(input("Enter Basic Pay: "))

    def calculate_gross_salary(self):
        self.gross_salary = self.bpay + 0.5 * self.bpay + 0.1 * self.bpay

    def display(self):
        print(f"ID: {self.eid}, Name: {self.ename}, City: {self.city}, Basic Pay: {self.bpay:.2f}, Gross Salary: {self.gross_salary:.2f}")

n = int(input("Enter number of employees: "))
employees = []
for _ in range(n):
    emp = Employee()
    emp.input_data()
    emp.calculate_gross_salary()
    employees.append(emp)

print("\nEmployee Details:")
for emp in employees:
    emp.display()