"""Write a program to count the occurrences of a given word in a text file. The given word is taken from
the user.
Sample Output: Enter file name: Sample.txt

Enter word to be searched: python
Occurrences of the “python” word: 5"""
file = input("Enter file name: ")
word = input("Enter word to be searched: ")
count = 0
with open(file,'r') as f1:
    content = f1.read()
    words = content.split()
for i in words:
    if i == word:
        count += 1
print("Occurence of the \""+str(word)+"\" word:",count)
