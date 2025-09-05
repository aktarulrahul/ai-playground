chai_type = "Ginger chai"
customer_name = "Myoria"

print(f"Customer: {customer_name} has ordered {chai_type}")

chai_description = "Aromatic and Bold"
print(f"chai_description: {chai_description[0:8:2]}") # Aoai
print(f"chai_description: {chai_description[:8]}") # Aromatic
print(f"chai_description: {chai_description[12:]}") # Bold
print(f"chai_description: {chai_description[::-1]}") # reverse

label_text = "chai Speécial"
print(f"Not encoded label_text: {label_text}")
encoded_text = label_text.encode("utf-8")
print(f"encoded_text: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"decoded_text: {decoded_text}")

