#write program using functions to determine sum of the following series up to nth term taken from user: (you may write as many functions as per your requirements)
#a) 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n
def s1(n):
    Sum = 0
    for i in range(1,n+1):
        l = ((-1)**(i+1))/i
        Sum += l
    print(Sum)
n = int(input("Enter the no. of terms (n) :"))
s1(n)