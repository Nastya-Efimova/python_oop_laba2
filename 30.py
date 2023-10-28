class User:
    __id = None

    def __init__(self):
        pass
    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id

class Employee(User):
    def __init__(self):
        pass
    def setName(self, name):
        self.__name = name
    def setSurname(self, surname):
        self.__surname = surname
    def setSalary(self, salary):
        self.__salary = salary

    def getName(self):
        return self.__name
    def getSurname(self):
        return self.__surname
    def getSalary(self):
        return self.__salary

stuff = Employee()

stuff.setId(1)
stuff.setName('Nastya')
stuff.setSurname('Efimova')
stuff.setSalary(123563)

print(  stuff.getId(),
        stuff.getName(),
        stuff.getSurname(),
        stuff.getSalary())