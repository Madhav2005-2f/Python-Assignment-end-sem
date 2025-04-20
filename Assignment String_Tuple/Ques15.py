#Write a program to swap the first and last characters of a string.
#Input: "Hello"
#Output: "oellH"
def swap_string(s):
    return s[-1] + s[1:-1] + s[0]
print(swap_string(input("Enter the string: ")))