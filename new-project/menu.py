class MenuItem:
    """model each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """models the Menu with drinks."""
    def __init__(self):
        self.Menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0)
        ]

    def get_items(self):
        """return all the name of the available menu items"""
        options = ""
        for items in self.Menu:
            options += f"{items.name}/"
        return options

    def find_drink(self,order_name):
        """Searches the menu for a particular drink"""
        for items in self.Menu:
            if items.name == order_name:
                return items
            else:
                print("Sorry that item is not available. ")



