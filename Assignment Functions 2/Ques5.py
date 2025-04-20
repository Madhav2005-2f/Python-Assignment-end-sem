"""Write a program to perform addition and multiplication of two 3 x 3 matrix."""
def add(m1,m2):
    mat = []
    for i in range(3):
        row = []
        for j in range(3):
            c = m1[i][j] + m2[i][j]
            row.append(c)
        mat.append(row)
    print(mat)
    
def multi(m1,m2):
    mat = []
    for i in range(3):
        row = []
        s = 0
        for j in range(3):
            c = m1[i][j] * m2[j][i]
            s += c
        print(s)
        row.append(s)
        mat.append(row)
    print(mat)
mat1 = [[2, 4, 6], [1, 3, 5], [7, 1, 6]]
mat2 = [[1, 3, 7], [7, 4, 5], [8, 9, 2]]
'''for i in range(1,3):
    for j in range(1,4):
        row = []
        for k in range(1,4):
            print("Enter the element",k,"of row",j,"of matrix",i,":",end="")
            a = int(input(""))
            row.append(a)
        if i == 1:
            mat1.append(row) 
        else:
            mat2.append(row)'''
        
print(mat1)
print(mat2)
#add(mat1,mat2)     
multi(mat1,mat2)
