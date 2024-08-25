from inventory import Inventory
from item import Item

def main():
    def add_item():
        print("Add a new item")
        name = input("Item name: ")
        price = float(input("Price per item: "))
        quantity = int(input("Quantity: "))
        my_inventory.add_item(Item(name, quantity, price))
        print("Added successfully!")
    
    def update_item():
        print("Update an existing item")
        id = input("Id of the item to update:")
        name = input("Updated name(or leave blank to keep existing): ")
        price = float(input("Updated price(or leave blank to keep existing): "))
        quantity = int(input("Updated quantity(or leave blank to keep existing): "))
        my_inventory.update_item(id, name, price, quantity)
        print("Updated successfully!")
    
    def remove_item():
        id = int(input("Enter id of item to remove"))
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