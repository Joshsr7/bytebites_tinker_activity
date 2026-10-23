# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described
in the spec.

## Behavioral Instructions
- Model only the four classes listed in bytebites_spec.md: Customer, FoodItem, Menu, and Order. Do not add extra classes such as Cart, Payment, or Restaurant.
- Every attribute must trace back to a sentence in the feature request. FoodItem has name, price, category, and popularity. Customer has name and purchase history.
- Use composition. Menu holds a list of FoodItem objects, Order holds a list of FoodItem objects, and Customer holds a list of past Order objects. No class inherits from another.
- Put each behavior in the class that owns the data. Filtering and sorting belong to Menu. Computing the total belongs to Order. Checking whether a customer is real belongs to Customer.
- Keep methods short and readable. Sort and filter methods return a new list and never change the original menu.
- An empty order must total 0, not crash.
