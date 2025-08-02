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

    

                



if __name__ == "__main__":
    groceries = {
    "Salat": 2,
    "Tomato": 4,
    "Peach": 7
    }
    program = Fridge(groceries)
    program.main()
  