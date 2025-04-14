price = {"Maggi Noodles":0,"Nuts pkt":0,"Cold Drink":0,"Cadbury DM":0,"Ketchup Sauce":0,"Fruit Jam":0,"Wheat pkt":0} 
unit = {"Maggi Noodles":0,"Nuts pkt":0,"Cold Drink":0,"Cadbury DM":0,"Ketchup Sauce":0,"Fruit Jam":0,"Wheat pkt":0}

def totalP():
    totaL = 0
    for i in price:
        totaL += price[i] * unit[i]
    return totaL
    
def discount(totaL):
    if totaL < 1500:
        dp = "5%"
        disc = 0.05*totaL
    elif totaL > 1500 and totaL < 5000:
        dp = "10%"
        disc = 0.1*totaL
    elif totaL > 5000:
        dp = "15%"
        disc = 0.15*totaL
    else:
        disc = 0
    return disc,dp
def display():
    totaL = totalP()
    disc, dp= discount(totaL)
    print("\t\tEveryThing @ Single UMBRELLA Grocery Shop")
    print("\t\t\tCity: Jaipur")
    print("----------------------------------------------------------------------------------")
    print("Item\t\t\tPrice\tQuantity\tSubtotaL")
    print("----------------------------------------------------------------------------------")
    for i in price:
        print(f"{i}\t\t{price[i]}\t{unit[i]}\t\t{price[i]*unit[i]}")
    print("----------------------------------------------------------------------------------")
    print("totaL\t\t\t\t\t\t",totaL)
    print("Discount\t\t",dp,"\t\t\t-",disc)
    print("----------------------------------------------------------------------------------")
    print("Grand Total\t\t\t\t\t",totaL-disc)
    print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("Enter the price of each item :")
print("----------------------------------------------------------------------------------")
for i in price:
    price[i] = int(input(f"{i} : "))
print("----------------------------------------------------------------------------------")
print("Enter the quantity of each item :")
print("----------------------------------------------------------------------------------")
for i in unit:
    unit[i] = int(input(f"{i} : "))
print("----------------------------------------------------------------------------------")
display()