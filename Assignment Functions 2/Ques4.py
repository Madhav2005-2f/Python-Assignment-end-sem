"""Write a program using two array of numbers taken from user and merging the two lists such that merged list is in
the sorted order. Write functions to solve the above task."""
def lst(list1, list2):
    l = list1 + list2
    l.sort()
    print(l)
l1 = eval(input("Enter the array 1 :"))
l2= eval(input("Enter the array 2 :"))
lst(l1,l2)