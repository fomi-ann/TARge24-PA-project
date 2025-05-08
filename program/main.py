
from program.clientData.client_data import *
from Order import *
from Pizza import *
from PizzaBase import *
from Restaurant import *
from Topping import *
from program.clientData.guestClient import GuestClient


def add_pizza_class_to_order(name, crust, size):
    """
        Creates a new pizza class and
        adds the item into the order class item list
        using add_item method.
    """
    if name == 'Margherita':
        if crust == 'thin':
            return Margherita(ThinCrust(size))
        else:
            return Margherita(ThickCrust(size))
    if name == 'Pepperoni':
        if crust == 'thin':
            return Pepperoni(ThinCrust(size))
        else:
            return Pepperoni(ThickCrust(size))
    if name == 'BBQ Chicken':
        if crust == 'thin':
            return BBQChicken(ThinCrust(size))
        else:
            return BBQChicken(ThickCrust(size))
    if name == 'Four Cheese':
        if crust == 'thin':
            return FourCheese(ThinCrust(size))
        else:
            return FourCheese(ThickCrust(size))
    if name == 'Veggie Supreme':
        if crust == 'thin':
            return VeggieSupreme(ThinCrust(size))
        else:
            return VeggieSupreme(ThickCrust(size))


def ask_user_for_pizza_name(restaurant):
    """
    1. Creates a list of numbers from 1 to the length of the restaurants menu items.
    2. Asks the user for an input ranging from 1 to restaurant menu length.
    3. Prints invalid input in case of an invalid input.
    4. Returns the restaurant menu items position.
    """
    correct_inputs = []
    for x in range(1, len(restaurant.menu_items) + 1):
        correct_inputs.append(str(x))

    while True:
        name_nr = input(f"Please choose a pizza number from the listing (1 to {len(restaurant.menu_items)}): ")
        if user_input_control(name_nr, correct_inputs):
            return restaurant.menu_items[int(name_nr) - 1]
        else:
            print("Invalid input please try again.")


def ask_user_for_crust():
    """
    Asks the user to input thick or thin.
    Returns the input.
    """
    correct_inputs = ['thick', 'thin']
    while True:
        crust = input("Do you want a thick or thin crust?(thick/thin): ").lower()
        if user_input_control(crust, correct_inputs):
            return crust
        else:
            print("Please enter a valid input.")


def ask_user_for_pizza_size():
    """
    Asks the user to input 25 or 30.
    Returns the input as integer.
    """
    correct_inputs = ['25', '30']
    while True:
        size = input("What size do you want your pizza?(25/30): ")
        if user_input_control(size, correct_inputs):
            return int(size)
        else:
            print("Please enter a valid input.")

def ask_user_for_pizza_param(restaurant):
    """
    Creates 3 variables which the method sends to
    add pizza class to order method.
    """
    name = ask_user_for_pizza_name(restaurant)
    crust = ask_user_for_crust()
    size = ask_user_for_pizza_size()
    order.add_item(add_pizza_class_to_order(name,crust,size))

def confirm_order():
    option = input("Confirm order? (y/n): ").lower()
    if option == 'y':
        print("")
        print(f"Order nr: {order.id} confirmed! Thank you for your order.")
        print("")
        order.get_summary()
    if option == 'n':
        change_order()


def change_order():
    if not order.ordered_items:
        print("Your order is empty.")
        return

    option = input("Would you like to change/delete your order? (change/delete): ").lower()
    if option == 'change':
        print("\nYour current ordered items are:")
        for idx, pizza in enumerate(order.ordered_items, start=1):
            print(f"{idx}. {pizza.name}")

        try:
            choice = int(input("\nEnter the number of the pizza you want to delete: "))
            order.remove_item_by_index(choice - 1)

        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    restaurant = Restaurant("Pizza place")
    client = user_operation_check()
    order = Order(restaurant, client)

    print("")
    print(f"Hello {client.get_full_name()}! It is a perfect time to have some pizza!\nTake a look at our menu:")
    print("")
    for idx, item in enumerate(restaurant.menu_items, start=1):
        pizzaThin25 = add_pizza_class_to_order(item, 'thin', 25)
        pizzaThin30 = add_pizza_class_to_order(item, 'thin', 30)
        pizzaThick25 = add_pizza_class_to_order(item, 'thick', 25)
        pizzaThick30 = add_pizza_class_to_order(item, 'thick', 30)
        print(f"{idx}. {item}")
        print(f"Thin 25cm price: {pizzaThin25.price}€ - Calories: {pizzaThin25.calories} --- Thick 25cm price: {pizzaThick25.price}€ - Calories: {pizzaThick25.calories}")
        print(f"Thin 30cm price: {pizzaThin30.price}€ - Calories: {pizzaThin30.calories} --- Thick 30cm price: {pizzaThick30.price}€ - Calories: {pizzaThick30.calories}")
        print("-----------")

    while True:
        ask_user_for_pizza_param(restaurant)#pitsa sisestamine orderisse
        correct_inputs = ['yes', 'y', 'no', 'n']
        continue_check = input("Do you want to buy another pizza?(y/n): ").lower()
        if user_input_control(continue_check, correct_inputs):
            if continue_check in correct_inputs[0:2]:
                pass
            else:
                confirm_order()
                break


