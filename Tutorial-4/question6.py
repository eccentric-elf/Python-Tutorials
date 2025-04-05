class Mobile:
    def set_details(self, company, model, price):
        self.company, self.model, self.price = company, model, price
    
    def display_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Price: ${self.price}")

m = Mobile()
m.set_details("Apple", "iPhone 13", 999)
m.display_details()
