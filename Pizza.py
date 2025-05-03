import uuid

class PizzaBase:
    """
    General pizza base class.

    Define all ingredients needed to make a pizza base.
    Measurements are in grams (g).
    """
    def __init__(self, size, flour, water, yeast, salt, oil, sugar=0):
        self.size = size
        self.flour = flour
        self.water = water
        self.yeast = yeast
        self.salt = salt
        self.oil = oil
        self.sugar = sugar

    def __repr__(self):
        """Return a string representation of the pizza size."""
        return f"{self.size} cm pizza"

class ThinCrust(PizzaBase):
    """
    Set a thin crust pizza ingredients based on pizza size.

    Measurements are in grams (g).
    """
    def __init__(self, size):
        if size == 25:
            super().__init__(size, 130, 80, 1.5, 2.5, 12, 1.5)
        elif size == 30:
            super().__init__(size, 160, 100, 2, 3, 15, 2)

class ThickCrust(PizzaBase):
    """
    Set a thick crust pizza ingredients based on pizza size.

    Measurements are in grams (g).
    """
    def __init__(self, size):
        if size == 25:
            super().__init__(size, 180, 105, 2.5, 3, 12, 3)
        elif size == 30:
            super().__init__(size, 220, 130, 3, 4, 15, 4)

"""Topping calories dictionary."""
Topping_calories = {
    "fresh mozzarella": 2.8,
    "shredded cheese": 3,
    "pepperoni slices": 5,
    "crushed tomatoes": 0.4,
    "BBQ sauce": 1.2,
    "cooked chicken breast": 1.65,
    "red onion": 0.4,
    "bell pepper": 0.2,
    "mushrooms": 0.22,
    "black olives": 1.15,
    "fresh basil": 0.23,
    "olive oil": 8.84,
    "salt": 0,
    "tomato sauce": 0.7,
    "blue cheese": 3.5,
    "goat cheese": 2.9,
    "parmesan": 4.3
}

class Topping:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.calories = self.weight * Topping_calories.get(self.name)
        self._set_price()

    def _set_price(self):
        self.price = round(0.1 * self.weight, 2)

    def __repr__(self):
        return self.name

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

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)
            self._set_price()
            self.calculate_calories()

    def remove_topping(self, topping_name):
        """Remove a topping by its name."""
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
        super().__init__("Margherita", dough)
        self.add_topping(Topping("crushed tomatoes", 120))
        self.add_topping(Topping("fresh mozzarella", 125))
        self.add_topping(Topping("fresh basil", 6))
        self.add_topping(Topping("olive oil", 15))
        self.add_topping(Topping("salt", 1))
        self.price = 10 if dough.size == 25 else 12
        self.calculate_calories()

    def __repr__(self):
        toppings_str = ", ".join(t.name for t in self.toppings)
        return f"{self.name} pizza with {toppings_str} toppings"

class Pepperoni(Pizza):
    def __init__(self, dough):
        super().__init__("Pepperoni", dough)
        self.add_topping(Topping("tomato sauce", 100))
        self.add_topping(Topping("shredded cheese", 150))
        self.add_topping(Topping("pepperoni slices", 60))
        self.add_topping(Topping("salt", 1))
        self.price = 12 if dough.size == 25 else 15
        self.calculate_calories()

    def __repr__(self):
        toppings_str = ", ".join(t.name for t in self.toppings)
        return f"{self.name} pizza with {toppings_str} toppings"


class BBQChicken(Pizza):
    def __init__(self, dough):
        super().__init__("BBQ Chicken", dough)
        self.add_topping(Topping("BBQ sauce", 100))
        self.add_topping(Topping("cooked chicken breast", 120))
        self.add_topping(Topping("red onion", 40))
        self.add_topping(Topping("shredded cheese", 120))
        self.add_topping(Topping("salt", 1))
        self.price = 12 if dough.size == 25 else 14
        self.calculate_calories()

    def __repr__(self):
        toppings_str = ", ".join(t.name for t in self.toppings)
        return f"{self.name} pizza with {toppings_str} toppings"


class FourCheese(Pizza):
    def __init__(self, dough):
        super().__init__("Four Cheese", dough)
        self.add_topping(Topping("fresh mozzarella", 80))
        self.add_topping(Topping("shredded cheese", 60))
        self.add_topping(Topping("blue cheese", 40))
        self.add_topping(Topping("goat cheese", 40))
        self.add_topping(Topping("parmesan", 25))
        self.price = 12 if dough.size == 25 else 14
        self.calculate_calories()

    def __repr__(self):
        toppings_str = ", ".join(t.name for t in self.toppings)
        return f"{self.name} pizza with {toppings_str} toppings"


class VeggieSupreme(Pizza):
    def __init__(self, dough):
        super().__init__("Veggie Supreme", dough)
        self.add_topping(Topping("tomato sauce", 100))
        self.add_topping(Topping("shredded cheese", 130))
        self.add_topping(Topping("bell pepper", 40))
        self.add_topping(Topping("mushrooms", 40))
        self.add_topping(Topping("red onion", 30))
        self.add_topping(Topping("black olives", 20))
        self.add_topping(Topping("olive oil", 15))
        self.add_topping(Topping("salt", 1))
        self.prize = 8 if dough.size == 25 else 10
        self.calculate_calories()

    def __repr__(self):
        toppings_str = ", ".join(t.name for t in self.toppings)
        return f"{self.name} pizza with {toppings_str} toppings"

    if __name__ == '__main__':
        fourcheese = FourCheese(ThickCrust(30))
        print(f"{fourcheese.name}: {fourcheese.price}€, {fourcheese.calories} kcal")

        custom = Pizza("Custom pizza", ThinCrust(25))
        custom.add_topping(Topping("fresh mozzarella", 80))
        custom.add_topping(Topping("shredded cheese", 60))
        custom.add_topping(Topping("blue cheese", 40))
        custom.add_topping(Topping("goat cheese", 40))
        custom.add_topping(Topping("parmesan", 25))
        print(f"{custom.name}: {custom.price}€, {custom.calories} kcal")

        pizza1 = FourCheese(ThinCrust(25))
        print(pizza1.name, pizza1.toppings)
        pizza1.remove_topping("blue cheese")
        print(pizza1.name, pizza1.toppings)

        Pizza123 = Margherita(ThinCrust(25))
        Pizza456 = Margherita(ThinCrust(25))
        print(Pizza123.id)
        print(Pizza456.id)
        print(Pizza123 == Pizza456)

        pizza122 = Margherita(ThinCrust(25))
        print(pizza122)

