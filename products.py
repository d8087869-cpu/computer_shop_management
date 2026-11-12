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
            display_all_products(products)
            
        elif choise == "3":
            search_product(products)
            
        elif choise == "4":
            update_product(products, categories)
            
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
    
    
def display_all_products(products):
    print("\n==================== ALL PRODUCTS ====================")  
    print(f"{'ID':<5} {'NAME':<30} {'CATEGORY':<15} {'PRICE':<12} {'STOCK':<8}")
    print("-" * 75)

    found_products =False
    for product in products:
        if product in products:
            found_products = True
            print(
                f"{product['id']:<5} "
                f"{product['name']:<30} "
                f"{product['category']:<15} "
                f"{product['price']:<12.2f} "
                f"{product['stock']:<8}"
            )
    if not found_products:
        print("NO active product found.")
    print("=" *75)
    
    
def search_product(products):
    print("\n========== SEARCH PRODUCT ==========")
    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Category")
    
    choice = input("\nChoose search option: ")
    found_products =[]
    if choice == "1":
        try:
            product_id = int(input("Enter product ID: "))
        except ValueError:
            print("Invalid ID.")
            return
        for product in products:
            if product["id"] == product_id and product["active"]:
                found_products.append(product)
    elif choice == "2":
        name= input("Enter product name: ").strip().lower()
        if not name:
            print("search name cannot be empty.")
            return
        for product in products:
            if name in product["name"].lower() and product["active"]:
                found_products.append(product)
    
    elif choice == "3":
        category = input("Enter category: ").strip().lower()

        for product in products:
            if product["category"].lower() == category and product["active"]:
                found_products.append(product)
    else:
        print("Invalid search option")
        return
    
    if found_products:
        display_all_products(found_products)
        
    else:
        print("no products found.")
        
        
def find_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def update_product(products, categories):
    print("\n========== UPDATE PRODUCT ==========")

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    product = find_product_by_id(products, product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"\nProduct: {product['name']}")
    print("1. Update Name")
    print("2. Update Category")
    print("3. Update Price")
    print("4. Update Active Status")

    choice = input("\nChoose what to update: ")

    if choice == "1":
        name = input("Enter new name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        product["name"] = name

    elif choice == "2":
        display_categories(categories)

        category = input("Enter new category: ").strip()

        if category not in categories:
            print("Invalid category.")
            return

        product["category"] = category

    elif choice == "3":
        try:
            price = float(input("Enter new price: "))

            if price <= 0:
                print("Price must be positive.")
                return

        except ValueError:
            print("Invalid price.")
            return

        product["price"] = price

    elif choice == "4":
        print("1. Active")
        print("2. Inactive")

        status = input("Choose status: ")

        if status == "1":
            product["active"] = True

        elif status == "2":
            product["active"] = False

        else:
            print("Invalid status.")
            return

    else:
        print("Invalid option.")
        return

    print("\nProduct updated successfully!")