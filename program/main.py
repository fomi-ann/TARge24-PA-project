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

if __name__ == '__main__':
    restaurant = Restaurant("Pizza place")
    client = GuestClient('1234567890123456', 'Kevin', 'Randla')
    pizza_name = 'Margherita'
    pizza_crust = 0  # 0 for thin, 1 for thick
    pizza_size = 25
    order = Order(restaurant,client)
    add_pizza_class_to_order(pizza_name, pizza_crust, pizza_size)
    print(order)

