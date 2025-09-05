ingredients = ["water", "milk", "black team"]
ingredients.append("sugar")


# Operator overloading
base_liquids = ["water", "milk"]
extra_flavors = ["ginger"]

full_chai = base_liquids + extra_flavors
print(f"Mix: {full_chai}")

full_chai = base_liquids * 2
print(f"brew: {full_chai}")

full_chai = base_liquids.extend(extra_flavors)
print(f"extend with extra flavors: {base_liquids.extend(extra_flavors)}")
print(f"extend: {full_chai}")
print(f"base_liquids: {base_liquids}")

full_chai = base_liquids.append(extra_flavors)
print(f"append with extra flavors: {base_liquids.append(extra_flavors[0])}") # none
print(f"append: {full_chai}")
print(f"base_liquids: {base_liquids}")


# byte array
raw_spice_data = bytearray(b"cardamom")
print(f"raw_spice_data: {raw_spice_data}")
raw_spice_data.replace(b"card", b"ginger")
print(f"raw_spice_data: {raw_spice_data}")