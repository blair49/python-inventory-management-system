from inventory import Inventory
from item import Item

def main():

    def add_item():
        print("Add a new item")
        name = input("Item name: ")
        while True:
            price = input("Price per item: ")
            try:
                price = float(price)
                break
            except Exception:
                print("Invalid input!!\nPlease enter a valid number.")
        while True:
            quantity = input("Quantity: ")
            try:
                quantity = int(quantity)
                break
            except Exception:
                print("Invalid input!!\nPlease enter a valid number.")                
            
        my_inventory.add_item(Item(name, quantity, price))
        print("Added successfully!")
    
    def update_item():
        print("Update an existing item")
        id,name,price,quantity = None, None, None, None
        while True:
            id = input("Id of the item to update: ")
            try:
                id = int(id)
                break
            except Exception:
                print("Invalid input!!\nPlease enter a valid number.")
        
        name = input("Updated name(or leave blank to keep existing): ")
        while True:
            price = input("Updated price(or leave blank to keep existing): ")
            if not len(price): 
                break
            try:
                price = float(price)
                break
            except Exception:
                print("Invalid input!!\nPlease enter a valid number.")
        while True:
            quantity = input("Updated quantity(or leave blank to keep existing): ")
            if not len(quantity): 
                break
            try:
                quantity = int(quantity)
                break
            except Exception:
                print("Invalid input!!\nPlease enter a valid number.")
        
        my_inventory.update_item(id, name, price=price, quantity=quantity)
        print("Updated successfully!")
    
    def remove_item():
        id=None
        while True:
            id = input("Enter id of item to remove: ")
            try:
                id = int(id)
                break
            except Exception:
                print("Invalid input!!\nPlease enter a valid number.")
        my_inventory.remove_item(id)
        print("Removed successfully!")
    
    def view_inventory():
        my_inventory.view_inventory()
        print(f"Total inventory value: ₹{my_inventory.total_value()}")

    my_inventory = Inventory()
    print("Inventory Management System CLI")
    while True:
        print("\nWhat would you like to do:")
        print("1. Add item")
        print("2. Update item")
        print("3. Remove item")
        print("4. View inventory")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Please select a valid option")

if __name__ == "__main__":
    main()