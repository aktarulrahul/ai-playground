value = 13
divisor = 2
# remainder = value % divisor

# if remainder:
#   print(f"Not divisible by {divisor}")
# else:
#   print(f"Divisible by {divisor}")

if(remainder :=value % divisor):
  print(f"Not divisible by {divisor}")
else:
  print(f"Divisible by {divisor}")

available_sizes = ["small", "medium", "large"]
if(requested_size := input("Enter the size of the chai: ").lower()) not in available_sizes:
  print(f"Invalid size: {requested_size}")
else:
  print(f"Valid size: {requested_size}")
