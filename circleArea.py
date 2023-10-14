import math
def calculate_circle_area(radius):
    return  math.pi * (radius ** 2)

try:
    radius = float(input("Input the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is: {area}")
except ValueError:
    print("Please enter a valid number for the radius.")

