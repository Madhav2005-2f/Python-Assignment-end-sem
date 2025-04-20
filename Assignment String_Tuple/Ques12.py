#Write a program to extract digits from a given string and store them in a tuple.
def extract_digits(s):
    l = []
    for d in s:
        if d.isdigit():
            l.append(int(d))
    return tuple(l)
print(extract_digits(input("Enter the string: ")))