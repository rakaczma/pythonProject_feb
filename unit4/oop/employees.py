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

employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("natalia", "nowak", 60, 15200))

print("Lista płac")
print("-" * 50)

for e in employees:
    print(e.getfullname(), "wiek:", e.getage(), "lat, pensja:", e.getsalary(), "zł")