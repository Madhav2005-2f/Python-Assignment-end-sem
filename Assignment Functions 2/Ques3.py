"""Read fifteen numbers from user. Write a program to find out how many of them are positive, how many are
negative, how many are even and how many odd."""
def p3(l):
    neg = 0 
    pos = 0
    eve = 0 
    odd = 0 
    for i in l:
        if i< 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            pass
        if i%2 == 0 :
            eve +=1 
        else:
            odd += 1
    print("There are",neg,"negative numbers",pos,"positive numbers",eve,"even numbers",odd,"odd numbers in the list.")
        
            
l = []
for i in range(1,16):
    print("Enter the number",i,":",end='')
    a = int(input())
    l.append(a)

p3(l)