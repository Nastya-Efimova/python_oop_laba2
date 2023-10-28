class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.__capeFirst(self.name)

    def __capeFirst(self, str):
        return str

class Employee(User):
    def setEmployeeInfo(self, employee_id):
        self.employee_id = employee_id

employee = Employee()
employee.setName("Maria")
employee.setEmployeeInfo(34)
print(employee.getName())
print(employee.employee_id)