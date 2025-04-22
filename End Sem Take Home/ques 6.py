import csv
#Uncomment the lines below when running the program for the first time 
# f1 = open("books.csv","w",newline='')
# b = csv.writer(f1)

# b.writerow(["Accession No.","Book Title","Author","Price","Publisher","Year of Publish","Copies Left","Issued"])
# f1.close()

# f2 = open("members.csv","w",newline='')
# c = csv.writer(f2)
# c.writerow(["Member ID","Name","Age","Phone No.","Email"])
# f2.close()

# f3 = open("issue.csv","w",newline='')
# c = csv.writer(f3)
# c.writerow(["Member ID","Name","Book Accession No.","Book Title","Issue Date","Return Date","Dues to be paid"])
# f3.close()

def bookinfo():
    query = input("Enter the book accession number or title: ")
    found = False

    with open("books.csv", "r") as f:
        rdr = csv.reader(f)
        next(rdr)
        for row in rdr:
            if row and (query.lower() in row[0].lower() or query.lower() in row[1].lower()):
                print("----------------------------------------------------------------------------")
                print("|--> Accession No.   :", row[0])
                print("|--> Book Title      :", row[1])
                print("|--> Author          :", row[2])
                print("|--> Price           :", row[3])
                print("|--> Publisher       :", row[4])
                print("|--> Year of Publish :", row[5])
                print("|--> Copies Left     :", row[6])
                print("|--> Issued          :", row[7])
                print("----------------------------------------------------------------------------")
                found = True
                break

    if not found:
        print("Book not found.")

def addbook():
    f = open("books.csv","a",newline='')
    b = csv.writer(f)
    print("----------------------------------------------------------------------------")
    print("Enter the books details :")
    print("----------------------------------------------------------------------------")
    accession = input("Enter the book accession number: ")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    price = input("Enter the book price: ")
    publisher = input("Enter the book publisher: ")
    year = input("Enter the book year of publish: ")
    copies = input("Enter the book copies left: ")
    issued = input("Enter the book issued: ")
    b.writerow([accession,title,author,price,publisher,year,copies,issued])
    f.close()
    print("----------------------------------------------------------------------------")
    print("Book added successfully")
    print("----------------------------------------------------------------------------")
def book_author():
    query = input("Enter the author name: ")
    print(f"All the books written by '{query}' are:")
    print("----------------------------------------------------------------------------")
    found = False
    with open("books.csv", "r") as f:
        rdr = csv.reader(f)
        next(rdr)  
        for row in rdr:
            if row and query.lower() in row[2].lower():
                print("|--> " + row[1])
                found = True

    if not found:
        print("No books found by this author.")
    print("----------------------------------------------------------------------------")
def no_of_books():
    f = open("books.csv","r")
    rdr = csv.reader(f)
    next(rdr)
    name = input("Enter the book title : ")
    for row in rdr:
        if row and name in row[1]:
            print("The book",name,"has",row[6],"copies left")
            break
def total_books():
    f = open("books.csv","r")
    rdr = csv.reader(f)
    next(rdr) # skip the header
    total = 0
    for row in rdr:
        total += int(row[6])
    print("The total number of books in the library is:",total)
    f.close() 
def member():
    name = input("Enter the member name or ID: ")
    found = False
    print("----------------------------------------------------------------------------")
    with open("members.csv", "r", newline='') as f:
        rdr = csv.reader(f)
        next(rdr) 

        for row in rdr:
            if row and (name == row[0] or name.lower() == row[1].lower()):
                print(f"The details of {name} are:")
                print("----------------------------------------------------------------------------")
                print("|--> Member ID:     ", row[0])
                print("|--> Name:          ", row[1])
                print("|--> Age:           ", row[2])
                print("|--> Phone Number:  ", row[3])
                print("|--> Email:         ", row[4])
                print("----------------------------------------------------------------------------")
                found = True
                break

    if not found:
        print("Member not found.")
    
def issue_book():
    book_found = False
    already_issued = False
    name = input("Enter the book title or accession ID: ")
    member = input("Enter the member name or ID: ")
    print("----------------------------------------------------------------------------")
    with open("books.csv", "r") as f:
        books = list(csv.reader(f))
    with open("issue.csv", "r") as f1:
        issued = list(csv.reader(f1))
    with open("members.csv", "r") as f2:
        members = list(csv.reader(f2))

    for row in books[1:]: 
        if name == row[1] or name == row[0]: 
            book_found = True
            for row1 in issued[1:]:
                if row[0] == row1[2] and (member == row1[1] or member == row1[0]):
                    print("The book is already issued to", row1[1])
                    already_issued = True
                    break
            if already_issued:
                break
            member_found = False
            for row2 in members[1:]:
                if member == row2[0] or member == row2[1]:
                    member_found = True
                    issue_date = input("Enter issue date (dd-mm-yyyy): ")
                    return_date = input("Enter return date (dd-mm-yyyy): ")
                    days = int(input("No. of days book issued: "))
                    print("----------------------------------------------------------------------------")
                    due = 1.5 * days
                    with open("issue.csv", "a", newline='') as f3:
                        writer = csv.writer(f3)
                        writer.writerow([row2[0], row2[1], row[0], row[1], issue_date, return_date, due])
                    for book_row in books:
                        if book_row[0] == row[0]:
                            book_row[6] = str(int(book_row[6]) - 1)
                            book_row[7] = str(int(book_row[7]) + 1)
                    with open("books.csv", "w", newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(books)

                    print(f"The book '{row[1]}' is issued to '{row2[1]}'.")
                    break

            if not member_found:
                print(f"{member} is not a member of this library.")

            break

    if not book_found:
        print(f"Book '{name}' not found.")

def return_book():
    book_name = input("Enter book name or accession number: ")
    member = input("Enter member name or ID: ")
    print("----------------------------------------------------------------------------")
    with open("books.csv", "r") as f_books:
        books = list(csv.reader(f_books))
    with open("issue.csv", "r") as f_issued:
        issued = list(csv.reader(f_issued))
    found = False
    header_books = books[0]
    header_issued = issued[0]
    books_data = books[1:]
    issued_data = issued[1:]
    updated_issued = []
    for row in issued_data:
        if row and (book_name == row[1] or book_name == row[2]) and (member == row[0] or member == row[1]):
            found = True
            dues = float(row[6])
            for book in books_data:
                if book_name == book[1] or book_name == book[0]:
                    book[6] = str(int(book[6]) + 1)
                    book[7] = str(int(book[7]) - 1)
                    break
        else:
            updated_issued.append(row)
    print("----------------------------------------------------------------------------")
    if found:
        print("Member has to pay his/her dues of",dues)
        paid = input("Has member paid the dues ?? (Y/N)")
        print("----------------------------------------------------------------------------")
        if paid.lower() == 'y':
            with open("issue.csv", "w", newline='') as f_issued:
                writer = csv.writer(f_issued)
                writer.writerow(header_issued)
                writer.writerows(updated_issued)
            with open("books.csv", "w", newline='') as f_books:
                writer = csv.writer(f_books)
                writer.writerow(header_books)
                writer.writerows(books_data)

            print(f"Book '{book_name}' returned successfully by member '{member}'.")
        else:
            print("Please clear the dues first.")
    else:
        print("----------------------------------------------------------------------------")
        print("Book not found as issued to this member.")
        print("----------------------------------------------------------------------------")
def total_dues():
    with open("issue.csv", "r") as f_issued:
        issued = list(csv.reader(f_issued))
        header_issued = issued[0]
        issued_data = issued[1:]
        total = 0
        member = input("Enter the member name or ID: ")
        print("----------------------------------------------------------------------------")
        for row in issued_data:
            if row and (member == row[0] or member == row[1]):
                total += float(row[6])
        print(f"Total dues of member '{member}' is {total}")
        print("----------------------------------------------------------------------------")

def search_members():
    with open("issue.csv", "r") as f_issued:
        issued = list(csv.reader(f_issued))
    issued_data = issued[1:]
    book = input("Enter the book name or ID: ")
    found = False
    print("----------------------------------------------------------------------------")
    print(f"Search Results for Book: '{book.title()}'")
    print("----------------------------------------------------------------------------")
    for row in issued_data:
        if row and (book == row[2] or book == row[3]):
            print(f"Member:      {row[1]} (ID: {row[0]})")
            print(f"Issued on:   {row[4]}")
            print(f"Return by:   {row[5]}")
            print(f"Due amount:  ₹{row[6]}")
            print("----------------------------------------------------------------------------")
            found = True

    if not found:
        print("No member found for the entered book.")
def search_books():
    with open("issue.csv", "r") as f_issued:
        issued = list(csv.reader(f_issued))
        issued_data = issued[1:]
        member = input("Enter the member name or ID: ")
        found = False
        print("----------------------------------------------------------------------------")
        print(f"Search Results for Member: '{member.title()}'")
        print("----------------------------------------------------------------------------")
        for row in issued_data:
            if row and (member == row[0] or member == row[1]):
                print(f"Book ID:      {row[2]}")
                print(f"Book Name:    {row[3]}")
                print(f"Issued on:   {row[4]}")
                print(f"Return by:   {row[5]}")
                print(f"Due amount:  ₹{row[6]}")
                print("----------------------------------------------------------------------------")
                found = True
        if not found:
            print("No book found for the entered member.")
def search_members_all():
    with open("members.csv","r") as f:
        members = list(csv.reader(f))
        members_data = members[1:]
        print("----------------------------------------------------------------------------")
        for row in members_data:
            if row:
                print(f"Member ID:    {row[0]}")
                print(f"Name:         {row[1]}")
                print(f"Age:          {row[2]}")
                print(f"Phone No:     {row[3]}")
                print(f"Email:        {row[4]}")
                print("----------------------------------------------------------------------------")
def add_member():
    with open("members.csv","r") as f1:
        members = list(csv.reader(f1))
    with open("members.csv", "a", newline='') as f:
        writer = csv.writer(f)
        name = input("Enter the member name: ")
        age = input("Enter the member age: ")
        phone = input("Enter the member phone number: ")
        email = input("Enter the member email: ")
        writer.writerow(["M"+str(len(members)), name, age, phone, email])
    print("Member added successfully with ID M"+str(len(members)))
def remove_member():
    with open("members.csv", "r") as f:
        members = list(csv.reader(f))
        member_id = input("Enter the member ID to be removed: ")
        for row in members:
            if row and row[0] == member_id:
                members.remove(row)
                print("Member removed successfully")
                break
        else:
            print("Member not found")
        with open("members.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(members)
        

def main():
    print("""----------------------------------------------------------------------------
    1. Display the book information
    2. Add a new book
    3. Display all the books of a author
    4. Display the number of books of a title
    5. Display total number of book in the library.
    6. Display details of library member
    7. Issue a book
    8. Return a book 
    9. Total dues to be paid by a member
    10. Display details of all members whom a particular book issued
    11. Display details of books issued by a member
    12. Display details of all members
    13. Add a new member
    14. Remove a member
    
----------------------------------------------------------------------------""")
    choice = int(input("Enter your choice :"))
    print("----------------------------------------------------------------------------")
    if choice == 1:
        bookinfo()
    elif choice == 2:
        addbook()
    elif choice == 3:
        book_author()
    elif choice == 4:
        no_of_books()
    elif choice == 5:
        total_books()
    elif choice == 6:
        member()
    elif choice == 7:
        issue_book()
    elif choice == 8:
        return_book()
    elif choice == 9:
        total_dues()
    elif choice == 10:
        search_members()
    elif choice == 11:
        search_books()
    elif choice == 12:
        search_members_all()
    elif choice == 13:
        add_member()
    elif choice == 14:
        remove_member()
    else:
        print("Invalid choice")
    print("----------------------------------------------------------------------------")
    if (input("Do you want to continue ?? (Y/N) :")).lower()=='y':
        main()
    else:
        exit()
main()