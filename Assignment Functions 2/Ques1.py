"""The information about colors is to be stored in bits of a char variable called color. The bit number 0 to 6, each
represent 7 colors of a rainbow, i.e. bit 0 represents violet, 1 represents indigo, and so on as given below. Write a
program using function that asks the user to enter a number and based on this number it reports which colours in the
rainbow does the number represents.
Red Orange Yellow Green Blue Indigo Violet"""
def rainbow(n):
    rainBow = {0:"Violet",1:"Indigo",2:"Blue",3:"Green",4:"Yellow",5:"Orange",6:"Red"}
    return rainBow[n]
n = int(input("Enter the number (0-6) :"))
print(n, "represents the",rainbow(n),"color of rainbow")