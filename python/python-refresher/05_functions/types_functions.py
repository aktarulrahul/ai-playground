# Types of functions in Python
# 1. pure vs impure functions
total = 20
def pure_function(x, y):
    return x + y
def impure_function(x):
    print(f"Input value is: {x}")
    global total
    return x * total


# 2. Recursive functions
def recursive_function(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_function(n - 1)
print(recursive_function(5))  # Output: 120

# 3. Anonymous functions (lambda functions)
chai_types = ['masala', 'ginger', 'tulsi', 'cardamom']
strong_chai = list(filter(lambda chai: chai in ['masala', 'ginger'], chai_types))
print(strong_chai)  # Output: ['masala', 'ginger']