class Employee:
    post = None
    name= None
    age= None
    salary= None

# работник 1
emp1 = Employee()
emp1.post = "engineer"
emp1.name = "Bob"
emp1.age = 27
emp1.salary = 90000

# работник 2
emp2 = Employee()
emp2.post = "baker"
emp2.name = "Toyota"
emp2.age = 45
emp2.salary = 87000

print(emp1.salary + emp2.salary)