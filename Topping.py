"""Topping calories dictionary."""
Topping_calories = {
    "Fresh mozzarella": 2.8,
    "Shredded cheese": 3,
    "Pepperoni slices": 5,
    "Crushed tomatoes": 0.4,
    "BBQ sauce": 1.2,
    "Cooked chicken breast": 1.65,
    "Red onion": 0.4,
    "Bell pepper": 0.2,
    "Mushrooms": 0.22,
    "Black olives": 1.15,
    "Fresh basil": 0.23,
    "Olive oil": 8.84,
    "Salt": 0,
    "Tomato sauce": 0.7,
    "Blue cheese": 3.5,
    "Goat cheese": 2.9,
    "Parmesan": 4.3
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