for token in range(1,11):
  print(f"Token {token} is dispensed")

print("All tokens are dispensed")


menu = ["coffee", "tea", "chai"]

for id, item in enumerate(menu):
  print(f"{id+1 if id+1 > 10 else '0' + str(id+1)}: {item}")


name = ['rahul', 'rohit', 'virat']
bills = [100, 200, 300]

for name, bill in zip(name, bills):
  print(f"{name} paid {bill}")


  