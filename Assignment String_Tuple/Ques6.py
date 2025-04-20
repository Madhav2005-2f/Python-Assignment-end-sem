#Write a program to find the index of the first occurrence of a given substring in a string.
sTr = input("Enter the main string: ")
subS = input("Enter the substring to find: ")

index = -1
for i in range(len(sTr)):
    if sTr[i:i + len(subS)] == subS:
        index = i
        break

if index != -1:
    print("The first occurrence of",subS,"is at index",index)
else:
    print(subS,"not found in the string.")