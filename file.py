import math
import cmath
import random
import statistics

def calculate_square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)
def calculate_area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)          
def calculate_perimeter_of_circle(radius):
    """Calculate the perimeter of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius     
def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    """Calculate the perimeter of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return 2 * (length + width) 
def calculate_area_of_triangle(base, height):
    """Calculate the area of a triangle given its base and height."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height
def calculate_perimeter_of_triangle(side1, side2, side3):
    """Calculate the perimeter of a triangle given its three sides."""
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Sides cannot be negative.")
    return side1 + side2 + side3
def calculate_volume_of_cylinder(radius, height):
    """Calculate the volume of a cylinder given its radius and height."""
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative.")
    return math.pi * (radius ** 2) * height 
def calculate_volume_of_sphere(radius):
    """Calculate the volume of a sphere given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return (4/3) * math.pi * (radius ** 3)