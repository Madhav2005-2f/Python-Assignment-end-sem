#write a program to merge the contents of two files into another file.
def merge_files(file1, file2):
    new_file = input("Enter the name of the new file: ")
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(new_file, 'w') as f3:
        f3.write(f1.read())
        f3.write(f2.read())

file1 = input("Enter the name of file1: ")
file2 = input("Enter the name of file2: ")
merge_files(file1, file2)