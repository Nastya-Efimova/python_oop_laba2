
class Employee:
    name= None
    salary= None

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_name(self):
        return self.name

    def show_salary(self):
        return self.salary

    def povishenie(self):
        return self.salary * 1.1

emp1 = Employee("Masha", 100000)

print(emp1.show_name(), emp1.show_salary(), emp1.povishenie())