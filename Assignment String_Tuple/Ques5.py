#Write a program to find the longest word in a given string.
sTr = input("Enter the string :")
L = sTr.split(" ")
largest = L[0]
for i in L:
    if len(i) > len(largest):
        largest = i
    
print("The largest word in the string is :",largest)