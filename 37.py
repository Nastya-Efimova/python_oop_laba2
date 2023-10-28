class User:
    def setName(self, name):
        if (self.notEmpty(name)):
            self.name = name

    def getName(self):
        return self.name

    def __notEmpty(stri):
        return len(stri) > 0


class Employee(User):
    def setSurname(self, surname):
        if (self.notEmpty(surname)):
            self.surname = surname

    def getSurname(self):
        return self.surname