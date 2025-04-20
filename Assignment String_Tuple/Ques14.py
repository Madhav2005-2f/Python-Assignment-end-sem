#Write a program to count the number of words in a given string.
def count_words(s):
    return len(s.split())
print("No. of words in the given string is",count_words(input("Enter the string: ")))