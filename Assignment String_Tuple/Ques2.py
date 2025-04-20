#Write a program to reverse a given string without using any inbuilt function.
sTr = input("Enter the string :")
rev = ""
for i in sTr:
    rev = i + rev 
    
print("Reversed string :",rev)