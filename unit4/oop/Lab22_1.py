class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname + " " + self.__lastname

    def getage(self):
        return self.__age

    def risesalary(self, percent=10):
        self.__salary *= percent / 100 + 1

def payroll(employees):
    print("Lista płac")
    print("-" * 50)
    for e in employees:
        print(e.getfullname(), "wiek:", e.getage(), "lat, pensja:", e.getsalary(), "zł")

employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("natalia", "nowak", 60, 15200))

payroll(employees)
employees[0].risesalary()
employees[2].risesalary(30)
payroll(employees)

