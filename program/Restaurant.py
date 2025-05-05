
from program.Pizza import *
from program.PizzaBase import *
from program.Order import Order


class Restaurant:
    def __init__(self, name):
        """Initialize Restaurant with given name."""
        self.name = name
        self.orders = []
        self.menu_items = []
        self.menu = {25: [], 30: []}

    def __repr__(self):
        return f'Welcome to {self.name}!'

    def add_menu_item(self, pizza: Pizza):
        """Add a pizza to the correct size group in the menu."""
        size = pizza.dough.size
        if size in self.menu:
            self.menu[size].append(pizza)


    def get_menu_item_name(self):
        """Return menu item name."""
        pizza_names = set(pizza.name for size in self.menu for pizza in self.menu[size])
        self.menu_items = list(pizza_names)


    def load_default_menu(self):
        """Add all pizza types (classes) to the menu"""
        self.add_menu_item(Margherita(ThinCrust(25)))
        self.add_menu_item(Pepperoni(ThinCrust(25)))
        self.add_menu_item(BBQChicken(ThinCrust(25)))
        self.add_menu_item(FourCheese(ThinCrust(25)))
        self.add_menu_item(VeggieSupreme(ThinCrust(25)))

        self.add_menu_item(Margherita(ThinCrust(30)))
        self.add_menu_item(Pepperoni(ThinCrust(30)))
        self.add_menu_item(BBQChicken(ThinCrust(30)))
        self.add_menu_item(FourCheese(ThinCrust(30)))
        self.add_menu_item(VeggieSupreme(ThinCrust(30)))


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