class PizzaBase:
    def __init__(self, thickness, size):
        self.thickness = thickness
        self.size = size
        self.calories = 0
        self.price = 0

    def __repr__(self):
        return f"You chose a {self.size} size pizza with a {self.thickness} base. Pizza base price is: {self.price}"

    def calculate_price(self):
        if self.size == 25:
            if self.thickness == "thin":
                self.price = 5
            if self.thickness == "thick":
                self.price = 7
        if self.size == 30:
            if self.thickness == "thin":
                self.price = 7
            if self.thickness == "thick":
                self.price = 9