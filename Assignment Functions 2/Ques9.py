"""A common problem in statistics is that of generating frequency distribution of the given data. Assuming that the
data consists of 50 positive integers in the range 1 to 25, write a program using function that prints the number of
times each integer occurs in the data."""
def freq(L):
    unit = []
    for i in L :
        if i not in unit:
            print(i,"occurs", L.count(i),"times in data")
            unit.append(i)
            
lst = eval(input("Enter the list :"))
freq(lst)