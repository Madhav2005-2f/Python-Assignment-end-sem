"""The first difference D1 of a sequence A of N elements is obtained by subtracting each element, except the last,
from the next element in the array. The second difference D2 is defined as the first difference of Dl, and so on. For
example, if
A: 1,2,4,7,11,16, 22, then
D1: 1,2,3,4, 5, 6
D2: 1,1,1,1, 1
D3: 0,0,0, 0
Write a program using appropriate functions that reads a sequence of 15 elements and finds its first, second,
and third differences."""
def D(lst):
    l =[]
    for i in range(len(lst)-1):
        a = lst[i+1]-lst[i]
        l.append(a)
    return l

seq = eval(input("Enter the list of the sequcence in the list format :"))
D1 = D(seq)
D2 = D(D1)
D3 = D(D2)
print(D1)
print(D2)
print(D3)