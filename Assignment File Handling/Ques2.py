#Write a Python program to read last n lines of a file.
def read_lines(filename,n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in lines[-n:]:
            print(i, end='')
file = input("Enter the filename: ")
n = int(input("Enter the no. of lines to read from last : "))
read_lines(file,n)