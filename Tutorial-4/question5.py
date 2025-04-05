class Person:
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")

p1 = Person("John", 30, 50000)
p2 = Person("Emma", 28, 60000)

p1.display()
p2.display()
