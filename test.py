from Topping import Topping
from Restaurant import Restaurant
from PizzaBase import PizzaBase
from Pizza import Pizza
from Order import Order
from Client import Client


if __name__ == '__main__':
    restaurant = Restaurant("PizzaPlace")
    print(restaurant.name)

    thin_base = PizzaBase("Thin base", 25)
    thick_base = PizzaBase("Thick base", 25)
    print(thin_base.size)
    print(thick_base.size)

