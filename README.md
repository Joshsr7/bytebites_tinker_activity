# ByteBites Tinker

Backend logic for ByteBites, a campus food ordering app, built from a short feature request into a UML design, four Python classes, and a pytest suite.

## Files

- bytebites_spec.md: the client feature request and the four candidate classes
- ByteBites_Design_Reference.md: the ground rules given to the AI assistant
- draft_from_copilot.md: the first UML draft made without the reference file, with my review of what was wrong
- bytebites_design.md: the final verified UML diagram and how it differs from the draft
- models.py: Customer, FoodItem, Menu, and Order
- test_bytebites.py: the test suite

## Design

| Class | Stores | Behavior |
|-------|--------|----------|
| Customer | name, purchase history | add_order, is_verified |
| FoodItem | name, price, category, popularity | none, it only holds data |
| Menu | list of FoodItems | add_item, filter_by_category, sort_by_price, sort_by_popularity |
| Order | list of FoodItems | add_item, calculate_total |

## How to run

```
pip install -r requirements.txt
python models.py
python -m pytest
```

## Sample output

```
$ python models.py
Drinks: ['Large Soda', 'Iced Tea']
By price: ['Iced Tea', 'Large Soda', 'Chocolate Cake', 'Spicy Burger']
By popularity: ['Chocolate Cake', 'Spicy Burger', 'Large Soda', 'Iced Tea']
Order total: 15.0
Empty order total: 0
Ana verified before ordering: False
Ana verified after ordering: True
```

```
$ python -m pytest
11 passed in 0.06s
```

## Why this design fits the request

Each class matches one noun in the feature request, and each attribute matches a detail the request names. The first AI draft added User, Cart, and Payment classes plus loyalty points and coupons. Adding the reference file with clear scope rules brought the design back to exactly what the client asked for.
