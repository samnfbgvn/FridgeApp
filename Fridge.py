import requests
import json

class Fridge:
    def __init__(self, groceries):
        self.groceries = groceries

    def add_item(self, name, count):
        name = name.title() 
        if name in self.groceries:
            self.groceries[name] += count
        else:
            self.groceries[name] = count


    def log_groceries(self):   
        if not self.groceries:
            print("The fridge is empty.") 
        for name, quantity  in self.groceries.items():
            print(f"- {name}: {quantity } ks")

    
    def rename_item(self, old_name, new_name):
        old_name = old_name.title()
        new_name = new_name.title()

        if old_name in self.groceries:
            if new_name in self.groceries:
                print(f"Item '{new_name}' already exists.")
            else:
                self.groceries[new_name] = self.groceries.pop(old_name)
                print(f"Renamed '{old_name}' to '{new_name}'")    
        else:
            print(f"{old_name} does not exist in your fridge.")

    def remove_item(self, name, count):
        name = name.title()
        if name in self.groceries:
            if self.groceries[name] >= count:
                self.groceries[name] -= count
                if self.groceries[name] == 0:
                    del self.groceries[name]
            else:
                print(f"You only have {self.groceries[name]} of {name} you took too much.")
        else:
            print(f"{name} is not in your fridge.")


    def save_to_json(self, filename="groceries_in_fridge.json"):
        with open(filename, "w") as file:
            json.dump(self.groceries, file, indent=4)
        print("Fridge contents saved!")

    def load_from_json(self, filename="groceries_in_fridge.json"):
        try:
            with open(filename, "r") as file:
                self.groceries = json.load(file)
            print(f"Fridge contents loaded from {filename}!")
        except FileNotFoundError:
            print(f"No file named {filename} found. Starting with an empty fridge.")
            self.groceries = {}

    
