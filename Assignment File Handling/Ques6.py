#Write a program to copy one file into another file in reverse manner.
def rev(filename1,filename2):
    with open(filename1,"r") as f1, open(filename2,"w") as f2:
        content = f1.read()
        content2 =""
        for i in f1:
            content2 = i + content2
        f2.write(content2)
        print('Work done !!')
    
file1 = input("Enter the name of original file: ")
file2 = input("Enter the name of destination file: ")
rev(file1,file2)
