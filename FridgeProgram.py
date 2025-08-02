

class FridgeProgram:
    def __init__(self, groceries):
        self.groceries = groceries


    def get_user_input(self, message):
        response = input(message)
        return response

    def is_input_string(self, text):
        if text.isalpha():
            return True
        else:
            print("Your log needs to have only letters")
            return False

    def is_input_positive_digit(self, text):
        if text.isdigit() and int(text) > 0:
            return True
        else:
            print("Your log may have only positive number")
            return False
    
    def get_name_and_quantity_input(self):
        while True:
            name = self.get_user_input("Enter the name of the grocery: ")
            if not self.is_input_string(name):
                print("The grocery name must contain only letters.")
                continue
            break

        while True: 
            count = self.get_user_input("Enter the quantity: ")
            if not self.is_input_positive_digit(count):
                continue
            break

        return name.lower(), int(count)
    
######
    
    def add_item(self, name, count):
        name = name.title() 
        if name in self.groceries:
            self.groceries[name] += count
            return count
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

       

#####

    def main(self):
        answer = self.get_user_input("Do you wanna now what you have in fridge? Yes/No: ")
        if answer.title() == "Yes":
            print("Your storage:\n")
            self.log_groceries()
            print("\n")
        else:
            print("Alright, closing the fridge")
        
        self.handle_menu()



    def handle_menu(self):
        while True:
            answer = self.get_user_input(
                "Do you want something to 'Add' = 1, 'Delete' = 2," \
                " 'Rename' = 3, 'Show Items' = 4, 'Close' = 5 -> ")
            
            if answer == "1":
                name, count = self.get_name_and_quantity_input()
                self.add_item(name, count)
                self.log_groceries()

            elif answer == "2":
                name, count = self.get_name_and_quantity_input()
                self.remove_item(name, count)
                self.log_groceries()
                
            elif answer == "3":
                old_name = self.get_user_input("Which item do you want to rename? ")
                new_name = self.get_user_input("Enter new name: ")
                self.rename_item(old_name, new_name)
                self.log_groceries()

            elif answer == "4":
                print("Your items in fridge: ")
                self.log_groceries()
            
            elif answer == "5":
                print(" Closing the fridge.")
                return
            
            else:
                print(" Invalid input – please type a number between 1 and 5.")

       

                



if __name__ == "__main__":
    groceries = {
    "Salat": 2,
    "Tomato": 4,
    "Peach": 7
    }
    program = FridgeProgram(groceries)
    program.main()
  