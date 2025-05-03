
from Pizza import *
from Order import Order


class Restaurant:
    def __init__(self, name):
        """Initialize Restaurant with given name."""
        self.name = name
        self.orders = []
        self.menu_items = []
        self.menu_pizza_25 = []
        self.menu_pizza_30 = []

    def __repr__(self):
        return f'Restaurant {self.name}, Todays pizza choices for 25 / 30 cm; thin / thick crust: {self.get_menu_item_name()}'

    def add_menu_item(self, pizza: Pizza):
        """Add a menu item to the restaurant's menu"""

        self.menu_pizza_25.append(pizza)
        self.menu_pizza_30.append(pizza)




    def get_menu_item_name(self):
        """Return menu item name."""
        pizza_25 = '25 cm Pizzas: '
        pizza_30 = '30 cm Pizzas: '
        for pizza in self.menu_pizza_25:
            pizza_25 += f'{pizza.name} '
        for pizza in self.menu_pizza_30:
            pizza_30 += f'{pizza.name}'
        return pizza_25 + ' ' + pizza_30


    def load_default_menu(self):
        """Add all pizza types (classes) to the menu"""
        self.menu_pizza_25.append(Margherita(ThinCrust(25)))
        self.menu_pizza_25.append(Pepperoni(ThinCrust(25)))
        self.menu_pizza_25.append(BBQChicken(ThinCrust(25)))
        self.menu_pizza_25.append(FourCheese(ThinCrust(25)))
        self.menu_pizza_25.append(VeggieSupreme(ThinCrust(25)))

        self.menu_pizza_30.append(Margherita(ThinCrust(30)))
        self.menu_pizza_30.append(Pepperoni(ThinCrust(30)))
        self.menu_pizza_30.append(BBQChicken(ThinCrust(30)))
        self.menu_pizza_30.append(FourCheese(ThinCrust(30)))
        self.menu_pizza_30.append(VeggieSupreme(ThinCrust(30)))


    def place_order(self, order: Order):
        """Add the order to the restaurant's order list"""
        self.orders.append(order)

    def cancel_order(self, order: Order):
        """Cancel the order from the restaurant's list of orders"""
        if order in self.orders:
            self.orders.remove(order)
            print(f"Order {order.id} has been removed from the orders list.")
        else:
            print(f"Order {order.id} not found in the orders list.")

    def confirm_order(self, order):
        """Confirm an order by adding it to the restaurant's system"""
        if order.client and order.ordered_items:
            self.place_order(order)
            print(f"Order {order.id} confirmed and added to the restaurant's system.")
        else:
            print(f"Order {order.id} is invalid and cannot be confirmed.")