def display_products_menu():
    print("\n=================================")
    print("     PRODUCTS MANAGMENT")
    print("=================================")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Back to Main Menu")


def products_menu(products, categories):
    while True:
        display_products_menu()
        choise = input("\nChoose an option: ")
        if choise == "1":
            add_product(products, categories)
            
        elif choise == "2":
            print("Display All Products")
            
        elif choise == "3":
            print("Search Product")
            
        elif choise == "4":
            print("Update Product")
            
        elif choise == "5":
            print("Delete Product")
        
        elif choise == "6":
            break
        
        else:
            print("Invalid Option. Try Again")
            
            
def display_categories(categories):
    print("\nAvailable Categories:")

    for category in categories:
        print(f"- {category}")
        

def get_next_product_id(products):
    if not products:
        return 1
    highest_id = 0 
    for product in products:
        if product["id"] > highest_id:
            highest_id = product["id"]     
    return highest_id +1

def add_product(products, categories):
    print("\n========== ADD PRODUCT ==========")
    name = input("Product name: ").strip()
    if not name:
        print("product name cannot be empty.")
        return
    
    display_categories(categories)
    
    category = input("\nChoose category: ").strip().lower()
    if category not in [category.lower() for category in categories]:
        print("Invalid category.")
        return
    
    try:
        price =float(input("Product price: "))
        if price <= 0:
            print("price must be positive.")
            return
        
        stock = int(input("Initial stock: "))
        if stock < 0:
            print("Stock cannot be negative.")
            return
    except ValueError:
        print("Invalid number.")
        return
    
    product = {
        "id": get_next_product_id(products),
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
        "active": True
    }
    products.append(product)
    print("\nProduct added succeffully!")