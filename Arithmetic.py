# Arithmetic operators and Math Functions

import math

# Circle
radius = float(input("Enter a radius:"))

circumference = 2 * math.pi * radius

#area  = math.pi * radius * radius
area = math.pi * pow(radius, 2)

print(f"Circumference of circle: {round(circumference, 2)}cm")

print(f"Area of cicrle: {round(area, 2)}cm^2")

#Triangle

a = float(input("Enter Side A : "))
b = float(input("Enter Side B : "))

c = math.sqrt((pow(a, 2)) + (pow(b, 2)))

print(f"Side C = {round(c, 2)}")



