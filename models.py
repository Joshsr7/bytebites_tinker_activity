# ByteBites backend models
#
# Customer: a user with a name and a purchase history of past orders.
# FoodItem: one item for sale with a name, price, category, and popularity.
# Menu: the full collection of food items, filterable by category.
# Order: one transaction that holds selected items and computes the total.


class FoodItem:
    """One item for sale, like a Spicy Burger or a Large Soda."""

    def __init__(self, name, price, category, popularity):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity

    def __repr__(self):
        return f"FoodItem({self.name!r}, {self.price}, {self.category!r}, {self.popularity})"


class Menu:
    """The full collection of food items for sale."""

    def __init__(self, items=None):
        self.items = list(items) if items else []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        """Return a new list of items in the category, ignoring letter case."""
        wanted = category.strip().lower()
        return [item for item in self.items if item.category.lower() == wanted]

    def sort_by_price(self):
        """Return a new list from cheapest to most expensive."""
        return sorted(self.items, key=lambda item: item.price)

    def sort_by_popularity(self):
        """Return a new list from most to least popular."""
        return sorted(self.items, key=lambda item: item.popularity, reverse=True)


class Order:
    """One transaction that groups the items a customer picked."""

    def __init__(self, items=None):
        self.items = list(items) if items else []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        """Return the total cost, rounded to cents. An empty order totals 0."""
        return round(sum(item.price for item in self.items), 2)


class Customer:
    """A user with a name and a history of past orders."""

    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = list(purchase_history) if purchase_history else []

    def add_order(self, order):
        self.purchase_history.append(order)

    def is_verified(self):
        """A customer counts as a real user once they have a past order with items."""
        return any(order.items for order in self.purchase_history)


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 10.00, "Mains", 4.5)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.0)
    cake = FoodItem("Chocolate Cake", 6.50, "Desserts", 4.8)
    tea = FoodItem("Iced Tea", 3.00, "Drinks", 3.2)

    menu = Menu([burger, soda, cake, tea])
    print("Drinks:", [i.name for i in menu.filter_by_category("Drinks")])
    print("By price:", [i.name for i in menu.sort_by_price()])
    print("By popularity:", [i.name for i in menu.sort_by_popularity()])

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print("Order total:", order.calculate_total())
    print("Empty order total:", Order().calculate_total())

    ana = Customer("Ana")
    print("Ana verified before ordering:", ana.is_verified())
    ana.add_order(order)
    print("Ana verified after ordering:", ana.is_verified())
