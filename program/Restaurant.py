
from program.Pizza import *
from program.Order import Order



class Restaurant:
    def __init__(self, name):
        """Initialize Restaurant with given name."""
        self.name = name
        self.orders = []
        self.menu = []


    def __repr__(self):
        return f'Restaurant {self.name}, menu: {self.get_menu_item_name()}'

    def add_menu_item(self, pizza: Pizza):
        """Add a menu item to the restaurant's menu"""
        self.menu.append(pizza)


    def get_menu_item_name(self):
        """Return menu item name."""
        pizza_names = ''
        print(self.menu)
        for pizza in self.menu:
            pizza_names += f'{pizza.name}'
        return pizza_names


    def load_default_menu(self):
        """Add all pizza types (classes) to the menu"""
        self.add_menu_item(Margherita)
        self.add_menu_item(Pepperoni)
        self.add_menu_item(BBQChicken)
        self.add_menu_item(FourCheese)
        self.add_menu_item(VeggieSupreme)


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