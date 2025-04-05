class Student:
    def __init__(self, name, roll):
        self.name, self.roll = name, roll
    
    def dataprint(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

s1 = Student("Alice", 101)
s2 = Student("Bob", 102)

s1.dataprint()
s2.dataprint()
