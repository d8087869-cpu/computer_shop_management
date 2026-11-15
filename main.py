from mock_data import products, categories
from products import products_menu
from inventory import inventory_menu

def display_main_menu():
    
    print("\n=================================")
    print("       COMPUTER STORE SYSTEM")
    print("=================================")
    print("1. Products Management")
    print("2. Inventory Management")
    print("3. Sales Management")
    print("4. Reports")
    print("5. Exit")


def get_menu_choise():
    choise = input("\nChoose an option: ")
    return choise

def main():
    while True:
        display_main_menu()
        choise = get_menu_choise()
        
        if choise == "1":
            products_menu(products, categories)
                    
        elif choise == "2":
            inventory_menu(products)
        
        elif choise == "3":
            print("Salse Managment")
            
        elif choise == "4":
            print("Reports")
            
        elif choise == "5":
            print("Goodbey!")
            break
        else:
            print("Invalide option. please try again.")
            
if __name__ == "__main__":
    main()