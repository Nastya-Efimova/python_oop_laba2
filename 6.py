
class Employee:
    post = None
    name= None
    age= None
    salary= None

    def work(self, name, salary):
        return name + ' ' + salary


# работник 1
emp1 = Employee()
emp1.post = "engineer"
emp1.age = 27


print(emp1.work("John", "78 000"))


