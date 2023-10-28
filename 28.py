class User:
    name = None
    surname = None

class Employee:
    pass

class Employee(User):
    pass

worker = Employee()
worker.name = "Masha"
worker.surname = "John"
print("Имя:", worker.name, "\nФамилия:", worker.surname)