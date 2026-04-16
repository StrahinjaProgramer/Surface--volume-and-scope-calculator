import pyfiglet
import numpy as np

banner = pyfiglet.figlet_format("surface volume and scope calculator", font="slant")
print(banner)

# Get user input for is it a square or rectangle
shape = input("1) Square 2) rectangle: 3) qube (Enter 1, 2 or 3): ")

if shape == "1":
    a = np.array([float(input("Enter the length of the side of the square: "))])
    surface = a * a
    scope = 4 * a
    print("Surface area of the square is: ", surface)
    print("Scope of the square is: ", scope)
    input("Press Enter to finisth the program...")
if shape == "2":
    a = np.array([float(input("Enter the length of the rectangle: "))])
    b = np.array([float(input("Enter the width of the rectangle: "))])
    surface = a * b
    scope = a * 2 + b * 2
    print("Surface area of the rectangle is: ", surface)
    print("Scope of the rectangle is: ", scope)
    input("Press Enter to finisth the program...")
if shape == "3":
    a = np.array([float(input("Enter the length of the side of the cube: "))])
    b = np.array([float(input("Enter the width of the cube: "))])
    c = np.array([float(input("Enter the height of the cube: "))])
    surface = 2 * (a * b + a * c + b * c)
    scope = 4 * (a + b + c)
    volume = a * b * c
    print("Surface area of the cube is: ", surface)
    print("Scope of the cube is: ", scope)
    print("Volume of the cube is: ", volume)
    input("Press Enter to finisth the program...")
