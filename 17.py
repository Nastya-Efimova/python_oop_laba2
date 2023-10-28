
class Employee:
    __name= None
    __salary= None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        self.__age = age


emp = Employee('','', '')
emp.setName("Masha")
emp.setSalary(100000)
emp.setAge(17)

print(emp.getName())
print(emp.getSalary())
print(emp.getAge())
