class Item:
    def __init__(self, name:str, quantity:int, price:float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        return f"Name: {self.name} | Quantity: {self.quantity} | Price: ₹{self.price}"