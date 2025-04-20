#Write a program to find out the factorial and Fibonacci numbers of given number using functions
def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the number: "))
print("Factorial of", n, "is", factorial(n))
print("The "+str(n)+"th term of Fibonacci number at is", fibonacci(n))