class User :
    name = None
    position = None
    department = None

    def __init__(self,name, position, department):
        self.name = name
        self.position = position
        self.department = department

class Position:
    number = None

    def __int__(self, number):
        self.number = number

class Depsrtament():
    num = None
    name_dep = None

    def __int__(self, num, name_dep):
        self.num = num
        self.name_dep = name_dep

user = User('Masha', 'директор', '1A')
position1 = Position()
departament1 = Depsrtament()

print(user.name) #имя
print(user.position) #должность
print(user.department) #отдел