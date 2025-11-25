# Generators --> are used to save memory as they generate items on-the-fly and do not store the entire collection in memory.
# 1. Save Memory
# 2. you don't want the result immediately, but rather want to iterate over it later.
# 3. lazy evaluation
# yield is used to produce a series of values over time, pausing after each one until the next value is requested.

def serve_coffee():
  yield "cup 1: Espresso"
  yield "cup 2: Cappuccino"
  yield "cup 3: Latte"
  yield "cup 4: Americano"

# yield pauses the function, saving its state for the next call

stall = serve_coffee()
print(next(stall))  # Output: Espresso
print(next(stall))  # Output: Cappuccino
print(next(stall))  # Output: Latte
print(next(stall))  # Output: Americano

def get_coffee_list():
  return ["cup 1", "cup 2", "cup 3", "cup 4"]

# Generator version
def get_coffee_generator():
  for i in range(1, 5):
    yield f"cup {i}"

coffee = get_coffee_list()
print(coffee)  # Output: ['cup 1', 'cup 2', 'cup 3', 'cup 4']
# print(next(coffee))  # Raises TypeError

def coffee_refill_count():
  count = 1
  while True: # for loop can also be used with a predefined range
    yield f"Refill count: {count}"
    count += 1
  
refill_user_1 = coffee_refill_count()
refill_user_2 = coffee_refill_count()

# for _ in range(5):
#   print(next(refill_user_1))
# for _ in range(3):
#   print(next(refill_user_2))

def coffee_customers():
  print("Welcome to the Coffee Shop!")
  order = yield "Please place your order."
  while True:
    print(f"Preparing your {order}...")
    order = yield f"Your {order} is ready!"

stall = coffee_customers()
next(stall)  # Start the generator
print(stall.send("Espresso"))
print(stall.send("Latte"))
