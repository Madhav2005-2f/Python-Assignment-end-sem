#write program using functions to determine sum of the following series up to nth term taken from user: (you may write as many functions as per your requirements)
#c) 1 /1! + 2^2/2! + 3^3/3! + ...........
def fact(n):
    f = 1
    if n == 0 or n == 1:
        return f
    else:
        for i in range(1,n+1):
            f *= i
        return f
def s1(n):
    Sum = 0
    for i in range(1,n+1):
        l = i**i/fact(i)
        Sum += l
    print(Sum)
n = int(input("Enter the no. of terms (n) :"))
s1(n)