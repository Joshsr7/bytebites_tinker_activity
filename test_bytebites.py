from models import Customer, FoodItem, Menu, Order


def make_menu():
    return Menu([
        FoodItem("Spicy Burger", 10.00, "Mains", 4.5),
        FoodItem("Large Soda", 5.00, "Drinks", 4.0),
        FoodItem("Chocolate Cake", 6.50, "Desserts", 4.8),
        FoodItem("Iced Tea", 3.00, "Drinks", 3.2),
    ])


# Happy path: a $10 burger and a $5 soda should total $15.
def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(FoodItem("Spicy Burger", 10.00, "Mains", 4.5))
    order.add_item(FoodItem("Large Soda", 5.00, "Drinks", 4.0))
    assert order.calculate_total() == 15.00


# Edge case: an order with nothing in it should total 0 and not crash.
def test_order_total_is_zero_when_empty():
    assert Order().calculate_total() == 0


# Edge case: prices like 0.10 and 0.20 should not leave floating point leftovers.
def test_total_is_rounded_to_cents():
    order = Order([FoodItem("Gum", 0.10, "Snacks", 1.0), FoodItem("Mint", 0.20, "Snacks", 1.0)])
    assert order.calculate_total() == 0.30


# Filtering Drinks should return only the drink items.
def test_filter_by_category_returns_only_that_category():
    drinks = make_menu().filter_by_category("Drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]
    assert all(item.category == "Drinks" for item in drinks)


# Filtering should not care about letter case.
def test_filter_by_category_ignores_case():
    assert len(make_menu().filter_by_category("drinks")) == 2


# A category with no items should return an empty list, not an error.
def test_filter_by_missing_category_returns_empty_list():
    assert make_menu().filter_by_category("Breakfast") == []


# Sorting by price should go from cheapest to most expensive.
def test_sort_by_price_cheapest_first():
    prices = [item.price for item in make_menu().sort_by_price()]
    assert prices == sorted(prices)


# Sorting by popularity should put the highest rated item first.
def test_sort_by_popularity_highest_first():
    assert make_menu().sort_by_popularity()[0].name == "Chocolate Cake"


# Sorting should return a new list and leave the menu order unchanged.
def test_sorting_does_not_change_the_menu():
    menu = make_menu()
    original = [item.name for item in menu.items]
    menu.sort_by_price()
    assert [item.name for item in menu.items] == original


# A customer with no purchase history is not verified yet.
def test_new_customer_is_not_verified():
    assert Customer("Ana").is_verified() is False


# A customer with a past order counts as a real user.
def test_customer_with_past_order_is_verified():
    ana = Customer("Ana")
    ana.add_order(Order([FoodItem("Large Soda", 5.00, "Drinks", 4.0)]))
    assert ana.is_verified() is True
