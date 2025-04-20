#Write a program to count the frequency of each character in a string.
sTr = input("Enter the string :")
L = []
for i in sTr:
    if i not in L:
        print("The count of",i,"in the string :",sTr.count(i))
        L.append(i)