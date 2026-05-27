# square
square_side = float(input("what is the length of the sides of the square? "))

area_of_square = square_side * square_side
area_of_square_meters = area_of_square/10000

print(f"The area of the square is {area_of_square}")
print(f"The area of the square in meters is {area_of_square_meters}")

print("")   
# rectangle
rectangle_length = float(input("what is the length of the rectangle? "))
rectangle_width = float(input("what is the width of the rectangle? "))

area_of_rectangle = rectangle_length * rectangle_width
area_of_rectangle_meters = area_of_rectangle/10000

print(f"The area of the rectangle is {area_of_rectangle}")
print(f"The area of the rectangle in meters is {area_of_rectangle_meters}")

print("")
# circle
circle_radius = float(input("what is the radius of the circle? "))
area_of_circle = 3.14 * circle_radius * circle_radius
area_of_circle_meters = area_of_circle/10000

print(f"The area of the circle is {area_of_circle}")
print(f"The area of the circle in meters is {area_of_circle_meters}")