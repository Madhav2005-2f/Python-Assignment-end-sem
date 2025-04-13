filename = input("Enter file name: ")
f1 = open(filename,"r")
word = input("Enter word to be searched: ")
content = f1.read()
l_text = content.split()
count = 0 
for i in l_text:
    if word == i:
        count += 1
print('Occurrences of the “',word,'” word:', count)