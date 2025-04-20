#Write a Python program to append text to a file and display the text.
def append(filename):
    text = input("Enter the text to append: ")
    with open(filename, "a") as file:
        file.write(text + "\n")
        print("Text appended successfully.")
def display(filename):
    with open(filename, "r") as file:
        print(file.read())
file = input("Enter the file name: ")
append(file)
display(file)