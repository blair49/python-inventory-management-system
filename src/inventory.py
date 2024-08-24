from item import Item
class Inventory:
    def __init__(self) -> None:
        self.items = {}
    
    def add_item(self, newItem:Item):
        if newItem:
            self.items[newItem.name] = newItem
    
    def update_item(self, name:str, quantity:int=None, price:float=None):
        if self.items[name]:
            if quantity is not None:
                self.items[name].quantity=quantity
            if price is not None:
                self.items[name].price=price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def low_stock(self, threshold:int):
        print("---------")
        print("Low stock items")
        print("---------")
        for item in self.items:
            if self.items[item].quantity < threshold:
                print(self.items[item])
        print("---------")
        
    def total_value(self)->float:
        total = 0
        for item in self.items.values():
            total += item.price * item.quantity
        return total

    def view_inventory(self):
        print("---------")
        print("Inventory")
        print("---------")
        for item in self.items:
            print(self.items[item])
        print("---------")
        