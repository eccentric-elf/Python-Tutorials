x, y = map(int, input("Enter x and y coordinates: ").split())

if x > 0 and y > 0:
    print("Quadrant 1")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x > 0 and y < 0:
    print("Quadrant 4")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
else:
    print("On X-axis")
