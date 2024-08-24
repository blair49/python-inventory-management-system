from item import Item
class Inventory:
    def __init__(self) -> None:
        self.items = {}
    
    def add_item(self, newItem:Item):
        if newItem:
            newItem.id = len(self.items)
            self.items[newItem.id] = newItem
    
    def update_item(self, id:int, name:str=None, quantity:int=None, price:float=None):
        if self.items[id]:
            if name is not None:
                self.items[id].name=name
            if quantity is not None:
                self.items[id].quantity=quantity
            if price is not None:
                self.items[name].price=price

    def remove_item(self, id:int):
        if id in self.items:
            del self.items[id]

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
        