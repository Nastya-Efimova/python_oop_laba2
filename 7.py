
class Employee:
    post = None
    name= None
    age= None
    salary= None

    def names(self):
        print(self.name)

    def salarys(self):
        print(self.salary)


# работник 1
emp1 = Employee()
emp1.post = "engineer"
emp1.name = "Bob"
emp1.salary = 87000
emp1.age = 27

emp1.names()
emp1.salarys()



