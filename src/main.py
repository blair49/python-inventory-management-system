from inventory import Inventory
from item import Item

my_inventory = Inventory()
item1 = Item("iPhone", 12, 70000)
item2 = Item("PS5", 10, 50000)
my_inventory.add_item(item1)
my_inventory.add_item(item2)
my_inventory.view_inventory()
print(f"Total Value: ₹{my_inventory.total_value()}")
my_inventory.low_stock(10)

my_inventory.update_item("PS5", 5, 40000)
my_inventory.view_inventory()
print(f"Total Value: ₹{my_inventory.total_value()}")
my_inventory.low_stock(10)

my_inventory.remove_item("PS5")
my_inventory.view_inventory()
print(f"Total Value: ₹{my_inventory.total_value()}")
my_inventory.low_stock(10)