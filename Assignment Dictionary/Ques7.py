#Write a program to multiply member(s) in a set
def multi_set(set):
    prod = 1
    if len(set) > 0:
        for i in set:
            prod *= i
    return prod

set = {112, 114, 115, 116, 118}
print(multi_set(set))