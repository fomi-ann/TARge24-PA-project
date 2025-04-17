class PizzaBase:
    def __init__(self, thickness, size):
        self.thickness = thickness
        self.size = size
        self.calories = 0
        self.prize = 0


class Pizza:
    def __init__(self, name, dough: PizzaBase):
        self.name = name
        self.toppings = []
        """List with topping objects"""
        self.prize = 0
        self.calories = 0
        self.dough = dough

    def __repr__(self):
        return f'({self.dough.size} cm {self.name} pizza with {self.dough.thickness}. Prize: {self.prize})'

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.pizzas = []
        """List with Pizza objects"""

    def create_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)


class Topping:
    def __init__(self, name, weight, amount):
        self.name = name
        self.weight = weight
        self.amount = amount
        self.calories = 0
        self.prize = 0


class Order:
    def __init__(self, client_id):
        self.client = client_id
        self.order_id = None
        """Random generated ID"""
        self.ordered_items = []

    def add_item(self, item):
        self.ordered_items.append(item)

class Client:
    def __init__(self, name):
        self.name = name
        self.id = None
        """Random generated ID"""


if __name__ == '__main__':
    restaurant = Restaurant("PizzaPlace")
    print(restaurant.name)

    thin_base = PizzaBase("Thin base", 25)
    thick_base = PizzaBase("Thick base", 25)
    print(thin_base.size)
    print(thick_base.size)

