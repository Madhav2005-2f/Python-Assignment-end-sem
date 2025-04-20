#Write a program using function to that will take shapes from users and finds the volumes , area and perimeter of various Geometrical Figures. The shape of geometrical figures may be entered and opted by users.
def sphere(r):
    vol = (4/3)*3.14*r**3
    area = 4*3.14*r**2
    perimeter = 0
    return vol, area, perimeter
def cube(a):
    vol = a**3
    area = 6*a**2
    perimeter = 12*a
    return vol, area, perimeter
def cylinder(r, h):
    vol = 3.14*r**2*h
    area = 2*3.14*r*h + 2*3.14*r**2
    perimeter = 2*3.14*r
    return vol, area, perimeter
def rectangle(l, b):
    vol = 0
    area = l*b
    perimeter = 2*(l+b)
    return vol, area, perimeter
def triangle(a, b, c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    perimeter = a+b+c
    return area, perimeter
def circle(r):
    area = 3.14*r**2
    perimeter = 2*3.14*r
    return area, perimeter

while True:
    print("1. Sphere")
    print("2. Cube")
    print("3. Cylinder")
    print("4. Rectangle")
    print("5. Triangle")
    print("6. Circle")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        r = float(input("Enter the radius of the sphere: "))
        vol, area, perimeter = sphere(r)
        print("Volume of the sphere: ", vol)
        print("Area of the sphere: ", area)
        print("Perimeter of the sphere: ", perimeter)   
    elif choice == 2:
        a = float(input("Enter the side of the cube: "))
        vol, area, perimeter = cube(a)
        print("Volume of the cube: ", vol)
        print("Area of the cube: ", area)
        print("Perimeter of the cube: ", perimeter)
    elif choice == 3:
        r = float(input("Enter the radius of the cylinder: "))
        h = float(input("Enter the height of the cylinder: "))
        vol, area, perimeter = cylinder(r, h)
        print("Volume of the cylinder: ", vol)
        print("Area of the cylinder: ", area)
        print("Perimeter of the cylinder: ", perimeter)
    elif choice == 4:
        l = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        vol, area, perimeter = rectangle(l, b)
        print("Area of the rectangle: ", area)
        print("Perimeter of the rectangle: ", perimeter)
    elif choice == 5:
        a = float(input("Enter the first side of the triangle: "))
        b = float(input("Enter the second side of the triangle: "))
        c = float(input("Enter the third side of the triangle: "))
        area, perimeter = triangle(a, b, c)
        print("Area of the triangle: ", area)
        print("Perimeter of the triangle: ", perimeter)
    elif choice == 6:
        r = float(input("Enter the radius of the circle: "))
        area, perimeter = circle(r)
        print("Area of the circle: ", area)
        print("Perimeter of the circle: ", perimeter)
    else:
        print("Invalid choice. Please choose a valid option.")
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        break
    