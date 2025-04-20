#Write a program to check whether a given key already exists in a dictionary or not.
def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
dic = eval(input("Enter the dictionary: "))
key = input("Enter the key: ")
t = check_key(dic, key)
if t:
    print(key, "is present in the dictionary")
else:
    print(key, "is not present in the dictionary")