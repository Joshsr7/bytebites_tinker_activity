# Draft UML, first pass without the reference file

Prompt used, with only bytebites_spec.md attached:

```
Here is the ByteBites feature request. I think the system needs four classes:
Customer, FoodItem, Menu, and Order. Draw a UML style class diagram with their
attributes, methods, and relationships.
```

Draft the assistant returned:

```mermaid
classDiagram
    class User {
        +int user_id
        +str email
        +str password_hash
        +login()
    }
    class Customer {
        +str name
        +list purchase_history
        +float loyalty_points
        +place_order()
    }
    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity
        +list allergens
    }
    class Menu {
        +list items
        +filter_by_category()
        +recommend_pairing()
    }
    class Cart {
        +list items
        +add_item()
    }
    class Order {
        +list items
        +float discount
        +calculate_total()
        +apply_coupon()
    }
    class Payment {
        +float amount
        +process()
    }
    User <|-- Customer
    Customer "1" --> "1" Cart
    Cart --> Order
    Order --> Payment
    Menu "1" o-- "many" FoodItem
```

## Review of this draft

- It added four things the spec never asked for: a User parent class with login and passwords, a Cart, a Payment class, and a pairing recommender.
- It added attributes that do not appear in the request: loyalty points, allergens, discounts, and coupons.
- It used inheritance from User, which the spec does not need.
- It is missing the Customer to Order history link that the spec uses to verify real users, and Order is not linked to FoodItem.
- The parts it got right were the four core attributes on FoodItem, a list of items on Menu, and filter_by_category on Menu.

I kept this draft only for comparison and wrote the final design in bytebites_design.md.
