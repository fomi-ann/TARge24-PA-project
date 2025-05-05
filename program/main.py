from numpy.ma.core import append

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
        if crust == 0:
            order.add_item(Margherita(ThinCrust(size)))
        else:
            order.add_item(Margherita(ThickCrust(size)))
    if name == 'Pepperoni':
        if crust == 0:
            order.add_item(Pepperoni(ThinCrust(size)))
        else:
            order.add_item(Pepperoni(ThickCrust(size)))
    if name == 'BBQChicken':
        if crust == 0:
            order.add_item(BBQChicken(ThinCrust(size)))
        else:
            order.add_item(BBQChicken(ThickCrust(size)))
    if name == 'FourCheese':
        if crust == 0:
            order.add_item(FourCheese(ThinCrust(size)))
        else:
            order.add_item(FourCheese(ThickCrust(size)))
    if name == 'VeggieSupreme':
        if crust == 0:
            order.add_item(VeggieSupreme(ThinCrust(size)))
        else:
            order.add_item(VeggieSupreme(ThickCrust(size)))


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
    correct_inputs = ['thick', 'thin']
    while True:
        crust = input("Do you want a thick or thin crust?(thick/thin): ").lower()
        if user_input_control(crust, correct_inputs):
            return crust
        else:
            print("Please enter a valid input.")


def ask_user_for_pizza_size():
    correct_inputs = ['25', '30']
    while True:
        size = input("What size do you want your pizza?(25/30): ")
        if user_input_control(size, correct_inputs):
            return int(size)
        else:
            print("Please enter a valid input.")


if __name__ == '__main__':
    restaurant = Restaurant("Pizza place")
    client = GuestClient('1234567890123456', 'Kevin', 'Randla')
    # print(restaurant.menu_items)
    # print(ask_user_for_pizza_name(restaurant))
    # print(ask_user_for_crust())
    print(type(ask_user_for_pizza_size()))
    # pizza_name = 'Margherita'
    # pizza_crust = 0  # 0 for thin, 1 for thick
    # pizza_size = 25
    order = Order(restaurant, client)
    # add_pizza_class_to_order(pizza_name, pizza_crust, pizza_size)
    # print(order)
