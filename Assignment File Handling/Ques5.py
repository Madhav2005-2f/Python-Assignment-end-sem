#Write a program which reads the contents of a text file and display only all the numbers which were present in the file.
def numbers(filename):
    with open(filename, 'r') as file:
        content = file.read().split()
        numbers = []
        for word in content:
            try:
                number = int(word)
                numbers.append(number)
            except ValueError:
                pass
        return numbers
file = input("Enter the filename: ")
num = numbers(file)
if num:
    print("The numbers in the given file are : ")
    for i in num:
        print(i, end=", ")
    print()