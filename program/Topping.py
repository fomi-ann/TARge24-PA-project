"""General toppings class."""
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
