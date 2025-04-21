#Write a program to read and store the records of students with each record containing name,age,phno and email id of a student. Write a program to read these records into a file and display them from file.

import pickle
def add():
    name = input("Enter Name of the student: ")
    age = int(input("Enter the age of the student: "))
    phn = input("Enter the phone no.: ")
    email = input("Enter the email ID: ")
    with open("Assignment File Handling\Students.dat", "ab") as file:
        data = [name, age, phn, email]
        pickle.dump(data, file)
def show():
    with open("Students.dat", "rb") as file:
        while True:
            try:
                content = pickle.load(file)
                if content[2] == Author:
                    count += 1
            except EOFError:
                break
    print(count)

print("""What do you want??
1. Enter data for new book
2. Count the no. of books by an author.""")
choice = int(input("Enter your choice: "))
if choice == 1:
    add()
elif choice == 2:
    author = input("Enter the name of author: ")
    countRec(author)
else:
    print("Invalid choice")
                
