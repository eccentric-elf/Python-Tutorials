from math import pi

def circarea(rad):
    area=pi*rad**2
    circ=2*pi*rad
    return f"area is: {area:.2f}\nperimeter is: {circ:.2f}"

rad=int(input("Enter the radius of the circle: "))
soln=circarea(rad)
print(soln)