#Write a program to check if a given string is a palindrome without using reversed() or slicing.
sTr = input("Enter the string :")
for i in range(len(sTr)):
    if sTr[i]!=sTr[len(sTr)-i-1]:
        print("The given string is not palindrome.")
        break
else:
    print("The given string is palindrome.")