from __future__ import annotations

from program.Pizza import *
from program.clientData import Client
import uuid

from Restaurant import *


class Order:
    def __init__(self, restaurant: Restaurant, client: Client):
        """Initialize the order details"""
        self.restaurant = restaurant
        self.client = client
        self.client_name = client.first_name + " " + client.last_name
        self.id = str(uuid.uuid4())
        self.total_price = 0
        self.total_calories = 0
        """Random generated ID"""
        self.ordered_items = []

    def __repr__(self):
        self.calculate_totals()
        return f"Order nr: {self.id}, {self.client}, total_price: {self.total_price}€, total_calories: {self.total_calories}"

    def add_item(self, pizza: Pizza):
        """Add a pizza item to current order if it's in the restaurant's menu"""
        pizza_list = self.restaurant.menu_items
        pizza_check = pizza.name in pizza_list
        if pizza_check:
            self.ordered_items.append(pizza)
            print(f"{pizza.name} was added to your order.")
        else:
            print(f"{pizza.name} is not in the restaurant's menu. Please choose something else.")

    def remove_pizza(self, pizza):
        """Remove a specific pizza instance from the order."""
        if pizza in self.ordered_items:
            self.ordered_items.remove(pizza)
            print(f"{pizza.name} was removed from your order.")
        else:
            print(f"{pizza.name} not found in this order.")

##
    def remove_item_by_index(self, index):
        """Remove a pizza from the order by index."""
        try:
            removed = self.ordered_items.pop(index)
            print(f"{removed.name} was removed from your order.")
        except IndexError:
            print("Invalid item number.")
##

    def calculate_totals(self):
        """Calculate the total cost and calories of all items in the order"""
        self.total_price = sum(pizza.price for pizza in self.ordered_items)
        self.total_calories = sum(pizza.calories for pizza in self.ordered_items)

    def get_summary(self):
        """Print the summary of the order"""
        self.calculate_totals()
        summary = f"Order ID: {self.id}\n"
        summary += f"Client: {self.client.get_full_name() if self.client else 'Unknown'}\n"
        summary += "Ordered items:\n"

        for pizza in self.ordered_items:
            summary += f" - {pizza.name} ({pizza.dough}): {pizza.price} EUR\n"

        summary += f"Total Price: {self.total_price} EUR\n"
        summary += f"Total Calories: {self.total_calories} kcal"
        print(summary)

    def clear_summary(self):
        summary = f"Order ID: {self.id} has been deleted"
        print(summary)








