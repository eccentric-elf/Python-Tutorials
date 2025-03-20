import math

def calculate_circle_area(radius_value):
    if radius_value < 0:
        return "Radius cannot be negative"
    
    area_result = math.pi * radius_value ** 2
    return area_result


radius_input = float(input("Enter the radius of the circle: "))

print(f"Area of the circle: {calculate_circle_area(radius_input):.2f}")

