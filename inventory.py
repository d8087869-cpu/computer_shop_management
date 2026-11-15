from products import display_all_products, search_product, find_product_by_id
from helpers import get_integer_input


def display_inventory_menu():
    print("\n=================================")
    print("       INVENTORY MANAGEMENT")
    print("=================================")
    print("1. Display All Inventory")
    print("2. Search Product in Inventory")
    print("3. Add Stock")
    print("4. Reduce Stock")
    print("5. Show Out of Stock Products")
    print("6. Show Low Stock Products")
    print("7. Back to Main Menu")


def inventory_menu(products):
    while True:
        display_inventory_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            display_all_products(products)

        elif choice == "2":
            search_product(products)

        elif choice == "3":
            add_stock(products)

        elif choice == "4":
            reduce_stock(products)

        elif choice == "5":
            print("Show Out of Stock Products")

        elif choice == "6":
            print("Show Low Stock Products")

        elif choice == "7":
            break

        else:
            print("Invalid option. Please try again.")
            

def add_stock(products):
    print("\n========== ADD STOCK ==========")
    product_id = get_integer_input("Enter product ID: ")
    if product_id is None:
        return
        
    product = find_product_by_id(products, product_id) 
    if product is None:
        print("product is not found")
        return   
              
    print(f"\nProduct: {product['name']}")
    print(f"Current stock: {product['stock']}")

    quantity = get_integer_input("Enter quantity to add: ")

    if quantity is None:
        return

    if quantity <= 0:
        print("Quantity must be positive.")
        return

    product["stock"] += quantity

    print("\nStock updated successfully!")
    print(f"New stock: {product['stock']}")
    
    
def reduce_stock(products):
    print("\n========== REDUCE STOCK ==========")

    product_id = get_integer_input("Enter product ID: ")
    if product_id is None:
        return

    product = find_product_by_id(products, product_id)
    if product is None:
        print("Product not found.")
        return

    print(f"\nProduct: {product['name']}")
    print(f"Current stock: {product['stock']}")

    quantity = get_integer_input("Enter quantity to reduce: ")
    if quantity is None:
        return

    if quantity <= 0:
        print("Quantity must be positive.")
        return

    if quantity > product["stock"]:
        print("Not enough stock available.")
        return

    product["stock"] -= quantity

    print("\nStock updated successfully!")
    print(f"New stock: {product['stock']}")