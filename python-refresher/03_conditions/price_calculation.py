size = input("Enter the size of the chai: ").lower()

if size == "small":
    price = 10
elif size == "medium":
    price = 15
elif size == "large":
    price = 20
else:
    print("Invalid size")
    price = 0

print(f"The price of the chai is {price}" if price > 0 else 'invalid size')