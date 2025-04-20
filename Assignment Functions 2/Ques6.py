"""The X and Y coordinates of 10 different points are entered through the keyboard. Write a program using function to find the distance of last point from the first point (sum of distance between consecutive points)."""
def dist(x1,y1,x2,y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    return d
l = []
for i in range(1,11):
    print("Enter the coordinates of point",i,", separated by comma :",end ='')
    x,y = eval(input())
    c = [x,y]
    l.append(c)

print(dist(l[0][0],l[0][1],l[9][0],l[9][1]))