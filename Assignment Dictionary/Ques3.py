#Write a program to merge two dictionaries taken from the user as input.
def merge_dict(dict1,dict2):
    merged_dict = {}
    for i in dict1:
        merged_dict[i] = dict1[i]
    for i in dict2:
        merged_dict[i]= dict2[i]
    return merged_dict
dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))
merged_dict = merge_dict(dict1,dict2)
print(merged_dict)
