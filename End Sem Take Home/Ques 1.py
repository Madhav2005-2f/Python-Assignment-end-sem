def dup_list(a,b):
    l = []
    for i in a:
        if i not in b:
            l.append(i)
    for i in b:
        if i not in a:
            l.append(i)
    print(l)

x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,76]
dup_list(x,y)