class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Designer(Employee):
    def work(self):
        print("Designer is creating designs")


employees = [
    Developer("Loveleen"),
    Designer("Alex")
]

for employee in employees:
    employee.work()