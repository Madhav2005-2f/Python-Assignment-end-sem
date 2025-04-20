#Write a program to merge two tuples and sort the result in ascending order without using sorted().
def merge_tuples(tup1, tup2):
    list1 = list(tup1)
    list2 = list(tup2)
    merged_list = list1 + list2
    return tuple(merged_list)
def tuple_sort(tup):
    lis = list(tup)
    sorted_list = []
    while lis:
        shortest = lis[0]
        for i in lis:
            if i < shortest:
                shortest = i
                
        sorted_list.append(shortest)
        lis.remove(shortest)
    return tuple(sorted_list)
t1 = eval(input("Enter the tuple 1: "))
t2 = eval(input("Enter the tuple 2: "))
t = merge_tuples(t1,t2)
print("Merged Tuple: ", t)
print("Sorted Tuple: ", tuple_sort(t))