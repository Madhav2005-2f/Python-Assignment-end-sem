""""Consider a binary file "Book.dat" which has structure [BookNo, BookName, Author, Cost].
i. create a function createFile() to input data for a record and add to Book.dat file.
ii. Write a function countRec(Author) which accepts the Author name as argument and count and return
number of books by the given Author which stored in binary book.dat file"""
import pickle
def createFile():
    bookNo = int(input("Enter Book No: "))
    bookName = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    cost = float(input("Enter Cost: "))
    with open("Assignment File Handling\Book.dat", "ab") as file:
        data = [bookNo, bookName, author, cost]
        pickle.dump(data, file)
def countRec(Author):
    count = 0
    with open("Book.dat", "rb") as file:
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
    createFile()
elif choice == 2:
    author = input("Enter the name of author: ")
    countRec(author)
else:
    print("Invalid choice")
                

