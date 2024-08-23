from item import Item
class Inventory:
    def __init__(self) -> None:
        self.items = []
    
    def add_item(self, newItem:Item):
        if newItem:
            self.items.append(newItem)
    
    def view_inventory(self):
        print(f"Items {self.items}")