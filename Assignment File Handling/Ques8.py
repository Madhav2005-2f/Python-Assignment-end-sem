#Write a program using function to count words in a text file those are ending with alphabet “o“ or “i“.
def o_or_i(filename):
    with open(filename, "r") as f1:
        content = f1.read().split()
        for i in content:
            if i[-1] in ['o', 'i']:
                print(i)

file = input("Enter the file name: ")
o_or_i(file)