"""General pizza base class."""
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

if __name__ == '__main__':
    pizza1 = ThinCrust(25)
    print (pizza1)
    pizza2 = ThinCrust(30)