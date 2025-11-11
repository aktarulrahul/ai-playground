available_snacks = ["somosa", "cookies"]

snacks_order = input("Enter the snack you want to order: ").lower()

if snacks_order in available_snacks:
    print(f"Your order of {snacks_order} is ready")
else:
    print(f"Sorry, {snacks_order} is not available")