# Comprehensions -> are a concise way to create lists, sets, dictionaries, or generators in Python using a single line of code.

# used ->
#  - filter items
#  - transform items
#  - create new collections
#  - flatten nested structures

# Q. What purpose do they serve?
# - cleaner code
# - faster execution

# Types of Comprehensions:
# 1. List Comprehensions -> [ expression for item in iterable if condition ]
squares = [x**2 for x in range(10)]
menu = [{
    'name': 'pasta',
    'price': 12,
    'available': True 
}, {
    'name': 'burger',
    'price': 8,
    'available': True
}, {
    'name': 'salad',
    'price': 10,
    'available': False
}, {
    'name': 'spaghetti pasta',
    'price': 15,
    'available': True
}]
# -------------------- Syntax --------------------
expensive_items = [item for item in menu if item['price'] >= 10 and item['available']]
# 2. Set Comprehensions -> { expression for item in iterable if condition }
unique_squares = {x**2 for x in range(10)}
favourite_chais = [
  "Masala Chai", "Green Tea", "Masala Chai",
  "Lemon Tea", "Green Tea", "Elaichi Chai"
]
unique_chais = {
  chai for chai in favourite_chais if len(chai) > 11
}
recipes = {
  "Masala Chai": ["water", "milk", "tea leaves", "spices", "sugar"],
  "Green Tea": ["water", "green tea leaves", "lemon", "honey"],
  "Lemon Tea": ["water", "black tea leaves", "lemon", "sugar"],
  "Elaichi Chai": ["water", "milk", "tea leaves", "elaichi", "sugar"]
}
# -------------------- Syntax --------------------
unique_spices = {
  spice
  for ingredients in recipes.values()
  for spice in ingredients
}
# 3. Dictionary Comprehensions -> { key: value for item in iterable if condition }
squared_dict = {x: x**2 for x in range(10)}
coffee_prices_bdt = {
  "Espresso": 150,
  "Cappuccino": 200,
  "Latte": 180,
  "Americano": 120
}
# --------------------- Syntax --------------------
coffee_prices_usd = {
  coffee: round(price / 122, 2) for coffee, price in coffee_prices_bdt.items() if price >= 60 # show only two decimal places
}
print(coffee_prices_usd) 

# 4. Generator Comprehensions -> ( expression for item in iterable if condition )
# Generators are used to save memory as they generate items on-the-fly and do not store the entire collection in memory.
squared_gen = (x**2 for x in range(10))
daily_sales =[10, 15, 7, 20, 13, 9, 25]
# -------------------- Syntax --------------------
total_sales_above_12 = sum(sale for sale in daily_sales if sale > 12)
print(total_sales_above_12)