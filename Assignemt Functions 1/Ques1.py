#Write a program using function to find out volume of 5 spheres.
def sphere_volume(radius):
    return (4/3)*3.14*radius**3
for i in range(5):
    radius = int(input("Enter the radius of the sphere: "))
    print("Volume of the sphere is: ", sphere_volume(radius))
