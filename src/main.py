from inventory import Inventory
from item import Item

my_inventory = Inventory()
item1 = Item("iPhone", 12, 70000)
item2 = Item("PS5", 10, 50000)
my_inventory.add_item(item1)
my_inventory.add_item(item2)
my_inventory.view_inventory()