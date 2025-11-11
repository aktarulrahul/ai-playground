masala_spices = ("cardamom", "cinnamon", "clove", "cumin")

(spice1, spice2, spice3, spice4) = masala_spices

print(f"spice1: {spice1}")
print(f"spice2: {spice2}")
print(f"spice3: {spice3}")
print(f"spice4: {spice4}")

ginger_ration, cardamon_ration = 2, 1
print(f"ginger_ration: {ginger_ration}")
print(f"cardamon_ration: {cardamon_ration}")
cardamon_ration, ginger_ration = ginger_ration, cardamon_ration
print(f"ginger_ration: {ginger_ration}")
print(f"cardamon_ration: {cardamon_ration}")

# membership

print(f"cardamon in masala_spices: {'cardamom' in masala_spices}")
print(f"cardamon in masala_spices: {'cardamom' not in masala_spices}")
print(f"cardamon in masala_spices: {'cardamom' in masala_spices}")