class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height, self.width, self.corner_x, self.corner_y = height, width, corner_x, corner_y
    
    def find_center(self):
        return (self.corner_x + self.width / 2, self.corner_y + self.height / 2)
    
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)

rect = Rectangle(10, 20, 0, 0)
print("Center:", rect.find_center())
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
