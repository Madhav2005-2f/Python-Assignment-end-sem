#Write a program to find the maximum and minimum values in a given tuple.
values = tuple(map(int, input("Enter the tuple values separated by spaces: ").split()))
maX = values[0]
miN = values[0]

for value in values:
    if value > maX:
        maX = value
    if value < miN:
        miN = value

print("Maximum value:",maX)
print("Minimum value:",miN)