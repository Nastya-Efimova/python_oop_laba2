class Student:
    name = 'Gleb'
    surname = 'viktoriv'

    def show(self):
        return self.name

    def __init__(self):
        print('+++')

user = Student()
user_2 = Student
print(user.name, user.surname)