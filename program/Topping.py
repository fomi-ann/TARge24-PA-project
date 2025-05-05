"""General toppings class."""
class Topping:
    def __init__(self, name, weight):
        """
        Initialize a pizza topping object.

        :param name: Name of the topping (not case-sensitive).
        :param weight: Weight of the topping in grams.
        """
        self.name = name
        self.weight = weight
        self._set_price()

        if name.lower() not in Topping_calories:
            raise ValueError(f"Unknown topping: {name}")
        self.calories = self.weight * Topping_calories[name.lower()]

    def _set_price(self):
        """Set the price of the topping based on it's weight."""
        self.price = round(0.1 * self.weight, 2)

    def __repr__(self):
        """Return a string representation of the topping."""
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


if __name__ == '__main__':
    topping1 = Topping("fresh mozzarella", 2.8)
    print(topping1)
