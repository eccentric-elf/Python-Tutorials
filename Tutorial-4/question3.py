class Car:
    def __init__(self, model, year, price):
        self.model, self.year, self.price = model, year, price
    
    def cost(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: ${self.price}")

car1 = Car("Toyota", 2020, 20000)
car2 = Car("Honda", 2022, 25000)

car1.cost()
car2.cost()
