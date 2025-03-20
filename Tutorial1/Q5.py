from math import *

def roots(a, b, c):
    disc = b**2 - 4*a*c

    if disc > 0:
        r1 = (-b + sqrt(disc)) / (2 * a)
        r2 = (-b - sqrt(disc)) / (2 * a)
        return f"2 real roots: {r1:.2f}, {r2:.2f}"
    elif disc == 0:
        r = -b / (2 * a)
        return f"1 real root: {r:.2f}"
    else:
        real = -b / (2 * a)
        imag = sqrt(abs(disc)) / (2 * a)
        return f"Complex roots: {real:.2f} ± {imag:.2f}i"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic.")
else:
    print(roots(a, b, c))
