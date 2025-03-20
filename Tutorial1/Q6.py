def rightangled(a, b, c):
    sides = sorted([a, b, c])
    
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        return "Yes, it's a right triangle."
    else:
        return "No, it's not a right triangle."

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print(rightangled(a, b, c))
else:
    print("Invalid triangle. Check side lengths.")
