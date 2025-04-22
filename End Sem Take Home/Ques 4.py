class Canteen:
    def __init__(self, name):
        self.name = name
        self.menu_items = {} 

    def Add_Item(self, item_name, price):
        self.menu_items[item_name] = price
        print(f"Item '{item_name}' added with price Rs.{price}")

    def Print_Menu(self):
        print(f"Canteen Name: {self.name}")
        print("Menu Items:")
        for item, price in self.menu_items.items():
            print(f"- {item}: Rs.{price}")

    def Compute_Cost(self):
        total = sum(self.menu_items.values())
        print(f"Total cost of all items in the menu: Rs.{total}")


my_canteen = Canteen("MNIT Food Plaza")
my_canteen.Add_Item("Samosa", 15)
my_canteen.Add_Item("Chai", 10)
my_canteen.Add_Item("Maggie", 40)
my_canteen.Add_Item("Sandwich", 35)

my_canteen.Print_Menu()

my_canteen.Compute_Cost()
