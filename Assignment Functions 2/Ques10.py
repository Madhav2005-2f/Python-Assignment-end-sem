"""The MANUFACTURING STARTTUP sells 5 types of memory chips through its retail outlets in 10 cities. The
weekly sales of the company are stored in a 5 x l 0 x 7 array SALES such that SALES( L, K, M ) denotes the sales of
the L memory chip in the K city on the M day of the week. Write a program that computes:
i) The total weekly sale of each type of memory chip
ii) The total weekly sale in each city and
iii) The average daily sale of the company"""

def total_sales_per_chip(SALES):
    total_per_chip = []
    for chip in range(len(SALES)):
        total = 0
        for city in range(len(SALES[chip])):
            for day in range(len(SALES[chip][city])):
                total += SALES[chip][city][day]
        total_per_chip.append(total)
    return total_per_chip

def total_sales_per_city(SALES):
    num_chips = len(SALES)
    num_cities = len(SALES[0])
    num_days = len(SALES[0][0])

    total_per_city = []
    for city in range(num_cities):
        total = 0
        for chip in range(num_chips):
            for day in range(num_days):
                total += SALES[chip][city][day]
        total_per_city.append(total)
    return total_per_city

def average_daily_sales(SALES):
    total_sales = 0
    count_days = 0
    for chip in SALES:
        for city in chip:
            for sale in city:
                total_sales += sale
                count_days += 1
    return total_sales / 7 

SALES = [[[1 for _ in range(7)] for _ in range(10)] for _ in range(5)]

chip_sales = total_sales_per_chip(SALES)
city_sales = total_sales_per_city(SALES)
average_sale = average_daily_sales(SALES)

print("Total weekly sale of each memory chip:")
for i, sale in enumerate(chip_sales, 1):
    print(f"Chip {i}: {sale}")

print("Total weekly sale in each city:")
for i, sale in enumerate(city_sales, 1):
    print(f"City {i}: {sale}")

print(f"Average daily sale of the company: {average_sale}")
