"""Fifteen numbers are taken from the user. The number to be searched is entered through the keyboard by the user.
Write a program using appropriate function(s) to find if the number to be searched is present in the array and if it is
present, display the number of times it appears in the list."""
def p2(l,n):
    if n in l:
        print("The number",n,"is present",l.count(n),"times in the array.")
    else:
        print("The number",n,"is not present in the array.")
l = []
for i in range(1,16):
    print("Enter the number",i,":",end='')
    a = int(input())
    l.append(a)
n = int(input("Enter the number to search :"))
p2(l,n)