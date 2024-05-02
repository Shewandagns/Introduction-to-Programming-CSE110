# Area of square
import math

def calculate_square_area(side_length):
    return side_length ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    # Square
    side_length_square = float(input("What is the length of a side of the square? "))
    area_square = calculate_square_area(side_length_square)
    print(f"The area of the square is: {area_square}")

    # Rectangle
    length_rectangle = float(input("What is the length of the rectangle? "))
    width_rectangle = float(input("What is the width of the rectangle? "))
    area_rectangle = calculate_rectangle_area(length_rectangle, width_rectangle)
    print(f"The area of the rectangle is: {area_rectangle}")

    # Circle
    radius_circle = float(input("What is the radius of the circle? "))
    area_circle = calculate_circle_area(radius_circle)
    print(f"The area of the circle is: {area_circle:.1f}")

if __name__ == "__main__":
    main()

"""
# Stretch Challenge
import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Function to calculate various areas and volumes from a single value
def calculate_areas_and_volumes(value):
    area_square = value ** 2
    area_circle = calculate_circle_area(value)
    volume_cube = value ** 3
    volume_sphere = (4 / 3) * math.pi * (value ** 3)
    return area_square, area_circle, volume_cube, volume_sphere

# Function to convert square centimeters to square meters
def convert_to_square_meters(area_in_square_cm):
    return area_in_square_cm / 10000

# Core Requirement: Calculate the area of a circle
radius_circle = float(input("What is the radius of the circle? "))
area_circle = calculate_circle_area(radius_circle)
print(f"The area of the circle is: {area_circle}")

# Stretch 2: Many areas from one value
value = float(input("What is the value to be used? "))
area_square, area_circle, volume_cube, volume_sphere = calculate_areas_and_volumes(value)

# Display results
print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {volume_sphere}")

# Stretch 3: cm -> m conversion
# Area of a square
side = float(input("What is the length of a side of the square (in cm)? "))
area_square = side ** 2
print(f"The area of the square is: {area_square} cm^2")
print(f"The area of the square is: {convert_to_square_meters(area_square)} m^2")

# Area of a rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area_rectangle = length * width
print(f"The area of the rectangle is: {area_rectangle} cm^2")
print(f"The area of the rectangle is: {convert_to_square_meters(area_rectangle)} m^2")

# Area of a circle
radius_circle = float(input("What is the radius of the circle (in cm)? "))
area_circle = calculate_circle_area(radius_circle)
print(f"The area of the circle is: {area_circle} cm^2")
print(f"The area of the circle is: {convert_to_square_meters(area_circle)} m^2")

"""
import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_areas_and_volumes(value):
    area_square = value ** 2
    area_circle = calculate_circle_area(value)
    volume_cube = value ** 3
    volume_sphere = (4 / 3) * math.pi * (value ** 3)
    return area_square, area_circle, volume_cube, volume_sphere

def convert_to_square_meters(area_in_square_cm):
    return area_in_square_cm / 10000

def main():
    # Stretch 1: Calculate the area of a circle
    radius_circle = float(input("What is the radius of the circle? "))
    area_circle = calculate_circle_area(radius_circle)
    print(f"The area of the circle is: {area_circle}")

    # Stretch 2: Many areas from one value
    value = float(input("What is the value to be used? "))
    area_square, area_circle, volume_cube, volume_sphere = calculate_areas_and_volumes(value)

    # Display results
    print(f"Area of a square: {area_square}")
    print(f"Area of a circle: {area_circle}")
    print(f"Volume of a cube: {volume_cube}")
    print(f"Volume of a sphere: {volume_sphere}")

    # Stretch 3: cm -> m conversion
    # Area of a square
    side = float(input("What is the length of a side of the square (in cm)? "))
    area_square = side ** 2
    print(f"The area of the square is: {area_square} cm^2")
    print(f"The area of the square is: {convert_to_square_meters(area_square)} m^2")

    # Area of a rectangle
    length = float(input("What is the length of rectangle (in cm)? "))
    width = float(input("What is the width of the rectangle (in cm)? "))
    area_rectangle = length * width
    print(f"The area of the rectangle is: {area_rectangle} cm^2")
    print(f"The area of the rectangle is: {convert_to_square_meters(area_rectangle)} m^2")

    # Area of a circle
    radius_circle = float(input("What is the radius of the circle (in cm)? "))
    area_circle = calculate_circle_area(radius_circle)
    print(f"The area of the circle is: {area_circle} cm^2")
    print(f"The area of the circle is: {convert_to_square_meters(area_circle)} m^2")

if __name__ == "__main__":
    main()
