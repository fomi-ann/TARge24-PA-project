import uuid
from PizzaBase import *
from Topping import *


class Pizza:
    """General pizza class."""
    def __init__(self, name, dough: PizzaBase):
        self.name = name
        self.dough = dough
        self.toppings = []
        self.price = 0
        self.calories = 0
        self.id = str(uuid.uuid4())

    def __eq__(self, other):
        return isinstance(other, Pizza) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)
            self._set_price()
            self.calculate_calories()

    def remove_topping(self, topping_name):
        """Remove a topping by it's name."""
        for topping in self.toppings:
            if topping.name == topping_name:
                self.toppings.remove(topping)
                self._set_price()
                self.calculate_calories()
                break


    def _set_price(self):
        """
        Set the price of the pizza.

        Base price of the pizza is 5 euros. If the size of the pizza is 30 cm,
        then 2 euros are added to the price and if the crust of the pizza is thick,
        then 1.5 euros are added to the price.

        Each topping costs 0.50 euros and the final price of the pizza is rounded
        to 2 places after comma.

        Prices are in euros.
        """
        base_price = 14
        if self.dough.size == 30:
            base_price += 2
        if isinstance(self.dough, ThickCrust):
            base_price += 1.5
        self.price = round(base_price, 2)

    def calculate_calories(self):
        """
        Calculate the calories of the pizza in kcal.

        Flour calories are estimated to be 3.6 kcal per gram and oil calories are
        estimated to be 8.8 kcal per gram. Topping calories are estimated to be
        2 kcal per gram per topping.

        :return: rounded calories of the pizza dough and toppings in kcal
        """
        dough_calories = self.dough.flour * 3.6 + self.dough.oil * 8.8
        toppings_calories = sum(t.calories for t in self.toppings)
        self.calories = round(dough_calories + toppings_calories)

class Margherita(Pizza):
    def __init__(self, dough):
        super().__init__('Margherita', dough)
        self.add_topping(Topping("Crushed tomatoes", 120))
        self.add_topping(Topping("Fresh mozzarella", 125))
        self.add_topping(Topping("Fresh basil", 6))
        self.add_topping(Topping("Olive oil", 15))
        self.add_topping(Topping("Salt", 1))
        self.price = 10 if dough.size == 25 else 12
        self.calculate_calories()

class Pepperoni(Pizza):
    def __init__(self, dough):
        super().__init__('Pepperoni', dough)
        self.add_topping(Topping("Tomato sauce", 100))
        self.add_topping(Topping("Shredded cheese", 150))
        self.add_topping(Topping("Pepperoni slices", 60))
        self.add_topping(Topping("Salt", 1))
        self.price = 12 if dough.size == 25 else 15
        self.calculate_calories()


class BBQChicken(Pizza):
    def __init__(self, dough):
        super().__init__('BBQ Chicken', dough)
        self.add_topping(Topping("BBQ sauce", 100))
        self.add_topping(Topping("Cooked chicken breast", 120))
        self.add_topping(Topping("Red onion", 40))
        self.add_topping(Topping("Shredded cheese", 120))
        self.add_topping(Topping("Salt", 1))
        self.price = 12 if dough.size == 25 else 14
        self.calculate_calories()


class FourCheese(Pizza):
    def __init__(self, dough):
        super().__init__('Four Cheese', dough)
        self.add_topping(Topping("Fresh mozzarella", 80))
        self.add_topping(Topping("Shredded cheese", 60))
        self.add_topping(Topping("Blue cheese", 40))
        self.add_topping(Topping("Goat cheese", 40))
        self.add_topping(Topping("Parmesan", 25))
        self.price = 12 if dough.size == 25 else 14
        self.calculate_calories()


class VeggieSupreme(Pizza):
    def __init__(self, dough):
        super().__init__('Veggie Supreme', dough)
        self.add_topping(Topping("Tomato sauce", 100))
        self.add_topping(Topping("Shredded cheese", 130))
        self.add_topping(Topping("Bell pepper", 40))
        self.add_topping(Topping("Mushrooms", 40))
        self.add_topping(Topping("Red onion", 30))
        self.add_topping(Topping("Black olives", 20))
        self.add_topping(Topping("Olive oil", 15))
        self.add_topping(Topping("Salt", 1))
        self.prize = 8 if dough.size == 25 else 10
        self.calculate_calories()