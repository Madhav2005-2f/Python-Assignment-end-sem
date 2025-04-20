#Write a program to find the sum of all numeric elements in a tuple.
# Input the tuple
values = tuple(map(int, input("Enter the tuple values separated by spaces: ").split()))
Sum = 0

for i in values:
    Sum += i    

print("The sum of all numeric elements in the tuple is:",Sum)