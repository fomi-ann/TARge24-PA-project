from Restaurant import *
from Pizza import Pizza
from PizzaBase import *
from client_data.Client import *
from Topping import *

if __name__ == '__main__':
    #0. Creating Restaurant
    resto = Restaurant("Pizza Place")
    resto.load_default_menu()
    resto.get_menu_item_name()

    clients = []


    # 1. Greet client and ask for credentials:
    while True:
        customer_first_name = input("Please enter your first name: ").strip()
        customer_last_name = input("Please enter your last name: ").strip()

        if customer_first_name and customer_last_name:
            break
        else:
            print("Both first and last names are required. Please try again.\n")

    print(f"Hello {customer_first_name} {customer_last_name}! It is a perfect time to have some pizza!\nTake a look at our menu:")

    for idx, item in enumerate(resto.menu_items, start=1):
        print(f"{idx}. {item}")

    client = Client(customer_first_name, customer_last_name)
    clients.append(client)

    # 2. Initialize order
    order = Order(resto, client)

    # 2.1 Ask for user input
    choice = int(input("Enter the number of the pizza you want: "))
    size = int(input("Choose size (25 or 30): "))
    crust_type = input("Choose crust (thin/thick): ").strip().lower()

    # 3: Create crust
    if crust_type == "thin":
        crust = ThinCrust(size)
    elif crust_type == "thick":
        crust = ThickCrust(size)
    else:
        print("Invalid crust type.")

