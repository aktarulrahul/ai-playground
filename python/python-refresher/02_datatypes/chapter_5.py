import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.499999999999

print(f"Ideal temp: {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference: {ideal_temp - current_temp}")
print(f"sys.float_info: {sys.float_info}")
print(f"Fraction(current_temp): {Fraction(current_temp)}")
print(f"Decimal(current_temp): {Decimal(current_temp)}")