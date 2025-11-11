is_boiling = False
str_count = "10"
print(f"Is boiling: {is_boiling}")
Total_actions =  int(str_count) + is_boiling # here is_boiling is converted to integer, upcasting to integer, here is_boiling is 0
print(f"Total actions: {Total_actions}")

is_boiling = True
print(f"Is boiling: {is_boiling}")
Total_actions =  int(str_count) + is_boiling # here is_boiling is converted to integer, upcasting to integer, here is_boiling is 1
print(f"Total actions: {Total_actions}")

# Downcasting
is_boiling = 1
print(f"Is boiling: {is_boiling}")
Total_actions =  int(str_count) + is_boiling # here is_boiling is converted to integer, upcasting to integer
print(f"Total actions: {Total_actions}")

milk_present = 0 # no milk 
sugar_present = None # no Sugar 
print(f"Is there milk? {bool(milk_present)}")
print(f"Is there sugar? {bool(sugar_present)}")