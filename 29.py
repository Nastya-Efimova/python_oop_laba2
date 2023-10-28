class User:
    def __init__(self):
        pass
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Employee(User):
    pass

stuff = Employee()

stuff.setName('John')
print(stuff.getName())