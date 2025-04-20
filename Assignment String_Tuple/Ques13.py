#Write a program to find the second largest element in a given tuple.
def second_largest(tup):
    if len(tup) < 2:
        return "No second largest element"
    elif len(tup) == 2:
        if tup[0] == tup[1]:
            return "No second largest element"
    else:
        return sorted(tup)[-2]
t = eval(input("Enter the tuple: "))
print("Second largest element of the tuple is: ",second_largest(t))