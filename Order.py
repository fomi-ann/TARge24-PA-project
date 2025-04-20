from Restaurant import Restaurant
from Pizza import Pizza
from Client import Client
import uuid


class Order:
    def __init__(self, restaurant: Restaurant):
        """Initialize the order details"""
        self.restaurant = restaurant
        self.client = None
        self.id = str(uuid.uuid4())
        self.total_price = 0
        self.total_calories = 0
        """Random generated ID"""
        self.ordered_items = []

    def add_item(self, pizza: Pizza):
        """Add a pizza item to current order if it's in the restaurant's menu"""
        if pizza in self.restaurant.menu:
            self.ordered_items.append(pizza)
            print(f"{pizza.name} was added to your order.")
        else:
            print(f"{pizza.name} is not in the restaurant's menu. Please choose something else.")

    def remove_item(self, pizza: Pizza):
        """Remove a specific pizza instance from the order."""
        if pizza in self.ordered_items:
            self.ordered_items.remove(pizza)
            print(f"{pizza.name} was removed from your order.")
        else:
            print(f"{pizza.name} not found in this order.")

    def set_client(self, client: Client):
        """Assign a client to the order"""
        self.client = client
        print(f"Client {self.client.name} with id: {self.client.id} placed an order: {self.ordered_items}")

    def calculate_totals(self):
        """Calculate the total cost and calories of all items in the order"""
        self.total_price = sum(pizza.prize for pizza in self.ordered_items)
        self.total_calories = sum(pizza.calories for pizza in self.ordered_items)

    def get_summary(self):
        """Print the summary of the order"""
        summary = f"Order ID: {self.id}\n"
        summary += f"Client: {self.client.name if self.client else 'Unknown'}\n"
        summary += "Ordered items:\n"

        for pizza in self.ordered_items:
            summary += f" - {pizza.name} ({pizza.dough.size}cm, {pizza.dough.thickness}): {pizza.prize} EUR\n"

        summary += f"Total Price: {self.total_price} EUR\n"
        summary += f"Total Calories: {self.total_calories} kcal"
        print(summary)








