with open("file1.txt","w") as f1:
    f1.write("Hello, world! \nMy name is Madhav Varshney. \nI am studying very hard to score good in my end semesgter exams. \nIf I don't study, I will fail in the end sem.")
    print("File created successfully.")

f1 = open("file1.txt","r")
f2 = open("file2.txt","w")
txt = f1.read()
words = txt.split()
print("Number of words in the file: ", len(words))
content = "Number of words in the file: "+ str(len(words)) + "\nStudent Name = Madhav Varshney \nStudent Roll Number = 2024UCE1176"
f2.write(content)
f1.close()
f2.close()

