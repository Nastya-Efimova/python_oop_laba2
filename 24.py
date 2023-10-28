class Employee:
    name = None
    salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

employees = [
    Employee('john', '12345'),    Employee('eric', '344444'),
    Employee('kyle', '1000000'),]
for employee in employees:
   print(employee.getName(), employee.getSalary())

