# Created by: Hiab G
# Date: Wed, Feb. 25th
# This program calculates the area and perimeter of a rectangle with user input
def main():
# Get user input for length and width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

# Formula to calculate area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

# Display the results
    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")


if __name__ == "__main__":
    main()
