from program.Restaurant import *
from Client import *




if __name__ == '__main__':
    # fourcheese = FourCheese(ThickCrust(30))
    # print(f"{fourcheese.name}: {fourcheese.price}€, {fourcheese.calories} kcal")
    #
    # custom = Pizza("Custom pizza", ThinCrust(25))
    # custom.add_topping(Topping("Fresh mozzarella", 80))
    # custom.add_topping(Topping("Shredded cheese", 60))
    # custom.add_topping(Topping("Blue cheese", 40))
    # custom.add_topping(Topping("Goat cheese", 40))
    # custom.add_topping(Topping("Parmesan", 25))
    # print(f"{custom.name}: {custom.price}€, {custom.calories} kcal")
    #
    # pizza1 = FourCheese(ThinCrust(25))
    # print(pizza1.name, pizza1.toppings)
    # pizza1.remove_topping("Blue cheese")
    # print(pizza1.name, pizza1.toppings)
    #
    pizza123 = Margherita(ThinCrust(25))
    pizza456 = Margherita(ThinCrust(30))
    # print(pizza123.name)
    # print(pizza456.id)
    # print(pizza123 == pizza456)
    #
    # pizza1.calculate_calories()
    # pizza123.calculate_calories()
    # pizza456.calculate_calories()
    #
    # print(pizza1.calories)
    # print(pizza123.calories)
    # print(pizza456.calories)
    #
    resto = Restaurant("Pizza Place")
    # print(resto.name)
    #
    # client1 = Client("Anna", "Fomina")
    # print(client1)
    #
    # order1 = Order(client1)
    # print(order1)
    #
    # order1.add_item(pizza123)
    # order1.add_item(pizza456)
    # print(order1.ordered_items)
    #
    # order1.calculate_totals()
    #
    # order1.get_summary()
    resto.load_default_menu()
    resto.get_menu_item_name()
    print(pizza123.name)
    # print(resto)