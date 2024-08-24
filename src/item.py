class Item:
    def __init__(self, id:int, name:str, quantity:int, price:float) -> None:
        self.id= id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Quantity: {self.quantity} | Price: ₹{self.price}"