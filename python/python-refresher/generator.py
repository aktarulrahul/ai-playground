# Generators --> are used to save memory as they generate items on-the-fly and do not store the entire collection in memory.
# 1. Save Memory
# 2. you don't want the result immediately, but rather want to iterate over it later.
# 3. lazy evaluation
# yield is used to produce a series of values over time, pausing after each one until the next value is requested.

def serve_coffee():
  yield "Espresso"
  yield "Cappuccino"
  yield "Latte"
  yield "Americano"

stall = serve_coffee()
print(next(stall))  # Output: Espresso
print(next(stall))  # Output: Cappuccino
print(next(stall))  # Output: Latte
print(next(stall))  # Output: Americano