#Write a program using own function Show_Words() to read lines from a text file to display those words which are less than 8 characters.
def Show_Words(filename):
    with open(filename, "r") as f1:
        content = f1.read().split()
        for i in content:
            if len(i) < 8:
                print(i)

file = input("Enter the file name: ")
Show_Words(file)