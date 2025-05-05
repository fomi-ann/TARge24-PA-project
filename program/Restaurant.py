from program.Pizza import *
from program.PizzaBase import *
from program.Order import Order


class Restaurant:
    def __init__(self, name):
        """Initialize Restaurant with given name."""
        self.name = name
        self.orders = []
        self.menu_items = ['Margherita', 'Pepperoni', 'BBQChicken', 'BBQChicken', 'FourCheese', 'VeggieSupreme']

    def __repr__(self):
        return f'Restaurant {self.name}, Todays pizza choices for 25 / 30 cm; thin / thick crust: {self.get_menu_item_name()}'

    def add_menu_item(self, pizza: Pizza):
        """Add a menu item to the restaurant's menu"""
        pass

    def get_menu_item_name(self):
        """Return menu item name."""
        pass

    def get_menu(self):
        """Prints out the menu items with their respective toppings."""
        pass

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
