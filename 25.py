class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

class EmployeesCollection:

    def __init__(self):
        self.__employees = []

    def add(self, employee):
        self.__employees.append(employee)

    def show(self):
        for employee in self.__employees:
            print(employee.getName())

po = EmployeesCollection()
po.add(Employee('maria', '123456'))
po.add(Employee('slava', '123456'))
po.add(Employee('nastya', '123456'))
po.show()