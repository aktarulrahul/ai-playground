users = [
  {
    "id": 1,
    "total": 100,
    "coupon": "20OFF",
  },
  {
    "id": 2,
    "total": 150,
    "coupon": "40OFF",
  }
]

discount_map = {
  "20OFF": (0.2, 0),
  "40OFF": (0.4, 0),
}

for user in users:
  percent, fixed = discount_map.get(user["coupon"], (0,0)) # (0,0) is the default value if the coupon is not found
  discount = user["total"] * percent + fixed
  user["total"] = user["total"] - discount
  print(f"User {user['id']} has paid {user['total']} after a coupon of {user['coupon']} with a discount of {discount}")
