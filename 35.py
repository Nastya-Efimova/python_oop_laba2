class User:
    __name = None
    __surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurname(self, surname):
        self.__surname = surname

    def getSurname(self):
        return self.__surname

class Employee(User):

    def getFull(self):
        return self.__name + ' ' + self.__surname

emp = Employee()

emp.setName('Gleb')
emp.setSurname('Viktorov')

print(emp.getName(), end=" ")
print(emp.getSurname())

print(emp.getFull())