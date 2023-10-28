
class Student:
    name = None
    surname = None

    def cape(self, str):
        return str.capitalize()

    def inic(self):
        return Name_1.name[0], Name_1.surname[0]


Name_1 = Student()
Name_1.name = "Alexander"
Name_1.surname = "Petrov"
print(Name_1.cape("александр"))
print(Name_1.inic())





