class Student:
    def readData(self, rollno, mark1, mark2):
        self.rollno, self.mark1, self.mark2 = rollno, mark1, mark2
    
    def computeTotal(self):
        return self.mark1 + self.mark2
    
    def printDetails(self):
        print(f"Roll No: {self.rollno}, Marks: {self.mark1}, {self.mark2}, Total: {self.computeTotal()}")

s = Student()
s.readData(101, 85, 90)
s.printDetails()
