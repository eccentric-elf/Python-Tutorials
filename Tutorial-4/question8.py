class Book:
    def get_details(self, title, author, cost):
        self.title, self.author, self.cost = title, author, cost
    
    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: ${self.cost}")

b = Book()
b.get_details("Python Programming", "John Doe", 29.99)
b.print_details()
