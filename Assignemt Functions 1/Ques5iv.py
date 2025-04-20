#write program using functions to determine sum of the following series up to nth term taken from user: (you may write as many functions as per your requirements)
#d) x -x^3/3! + x^5/5! - x^7/7! + .......... # (sin(x) series)
def fact(n):
    f = 1
    if n == 0 or n == 1:
        return f
    else:
        for i in range(1,n+1):
            f *= i
        return f
def s1(n,x):
    Sum = 0
    for i in range(1,n+1):
        l = ((-1)**(i+1))*(x**(2*i - 1))/fact(2*i-1)
        Sum += l
    print(Sum)
n = int(input("Enter the no. of terms (n) :"))
x = int(input("Enter the value of x :"))
s1(n,x)