from fridge import Fridge

# 1️⃣ Create a fridge and add some groceries
my_fridge = Fridge({})
my_fridge.add_item("Milk", 2)
my_fridge.add_item("Eggs", 12)

# 2️⃣ Save groceries to the JSON file
my_fridge.save_to_json()

print("\n--- Saved groceries to file ---\n")

# 3️⃣ Create a brand-new fridge (empty)
new_fridge = Fridge({})
new_fridge.load_from_json()  # Load from JSON file

print("\n--- Loaded groceries from file ---")
new_fridge.log_groceries()