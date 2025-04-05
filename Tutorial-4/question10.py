class Complex:
    def __init__(self, real, imag):
        self.real, self.imag = real, imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)
c3 = c1 + c2

print("Sum:", c3)
