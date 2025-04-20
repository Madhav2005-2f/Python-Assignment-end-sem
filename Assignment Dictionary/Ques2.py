#Create a function that can print a dictionary where the keys are numerical values between 1 and 6 and the values are cube of keys.
def cube_dict():
    cube_dict = {}
    for i in range(1,7):
        cube_dict[i]= i**3
    return cube_dict
print(cube_dict())