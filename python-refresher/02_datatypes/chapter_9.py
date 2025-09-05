essential_spices = {"cardamom", "cinnamon", "ginger"}
optional_spices = {"cloves", "ginger"}

all_spices = essential_spices.union(optional_spices)
print(f"all_spices: {all_spices}")

common_spices = essential_spices.intersection(optional_spices)
print(f"common_spices: {common_spices}")

diff_spices = essential_spices.difference(optional_spices) # essential_spices - optional_spices
print(f"diff_spices: {diff_spices}")

sub_spices = optional_spices.difference(essential_spices) # optional_spices - essential_spices
print(f"sub_spices: {sub_spices}")