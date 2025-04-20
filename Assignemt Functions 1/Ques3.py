#Find out the various roots of quadratic equation using appropriate functions
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        print("Roots are real and distinct")
    elif discriminant == 0:
        print("Roots are real and equal")    
    else:
        print("Roots are complex and distinct")
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
root1, root2 = find_roots(a, b, c)
print("Roots of the given eqn are:",root1,"and",root2)