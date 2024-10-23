# Prompt the user to enter the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the triangle is valid (sum of any two sides must be greater than the third side)
if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Invalid triangle. The sum of any two sides must be greater than the third side.")
else:
    # Determine the type of triangle
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")