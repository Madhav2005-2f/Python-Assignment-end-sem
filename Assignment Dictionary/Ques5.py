#Write a program to get the largest values from a dictionary that stores the numerical values in it using appropriate function.
#Input: {1: 10, 2: 20, 3: 30, 4:40, 5:50, 6:60}
#Output: 60
def largest(dict):
    keys = list(dict.keys())
    largest = dict[keys[0]]
    for key in keys:
        if dict[key] > largest:
            largest = dict[key]
    return largest

print(largest({1: 10, 2: 20, 3: 30, 4: 40, 5:50, 6:60}))  