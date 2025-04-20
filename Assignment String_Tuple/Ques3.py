#Write a program to replace all spaces in a string with underscores.
sTr = input("Enter the string :")
new_sTr = ""
for i in sTr:
    if i == " ":
        new_sTr += "_"
    else:
        new_sTr += i 
print("New String :",new_sTr)