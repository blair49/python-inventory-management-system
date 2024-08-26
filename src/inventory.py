import json
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
            if name is not None and len(name):
                self.items[id].name=name
            if quantity is not None and type(quantity) is int:
                self.items[id].quantity=quantity
            if price is not None and type(price) is float:
                self.items[id].price=price

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

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json_data = {id:vars(item) for id, item in self.items.items()}
            json.dump(json_data,file)
    
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                json_data = json.load(file)
                for item in json_data.values():
                    item = Item(item["name"], item["quantity"], item["price"], id=item["id"])
                    self.items[item.id] = item
        except FileNotFoundError:
            print(f"{filename} save file not found. Starting with an empty inventory.")
    