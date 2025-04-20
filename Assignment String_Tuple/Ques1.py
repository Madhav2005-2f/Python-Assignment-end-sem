#Write a program to count the number of vowels in a given string.
sTr = input("Enter the string :")
c = 0 
for i in sTr.lower():
    if i in ['a','e','i','o','u']:
        c += 1
print("No. of vowels in the given string is",c)