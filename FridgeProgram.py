
class FridgeProgram

    class Fridge(self, groceries)



groceries = {
    "Salat": 2,
    "Tomato": 4,
    "Peach": 7
}



def main():
    answer = input("Do you wanna now what you have in fridge? Yes/No: ")
    if answer.lower() == "yes":
        print("Your storage:\n")
        log_groceries()
        print("\n")
    else:
        print("Alright, closing the fridge")
    
    handle_menu()
  
   
def handle_menu():
    while True:
        answer = get_user_input("Do you want something to 'Add' = 1, 'Delete' = 2, 'Rename' = 3, 'Show Items' = 4, 'Close' = 5 -> ")
        if answer == "1":
            name, count = get_name_and_quantity_input()
            add_grocery_item(name.title(), count)
            log_groceries()

        elif answer == "2":
            name, count = get_name_and_quantity_input()
            substract_grocery_item(name.title(), count)
            log_groceries()
            
        elif answer == "3":
            name = get_user_input("Which item do you want to rename? ").title()
            rename(name)
            log_groceries()
        elif answer == "4":
            print("Your items in fridge: ")
            log_groceries()
        
        elif answer == "5":
            print(" Closing the fridge.")
            return
        
        else:
            print(" Invalid input – please type a number between 1 and 5.")

       

            

def get_user_input(message):
    response = input(message)
    return response


def get_name_and_quantity_input():
    while True:
        name = get_user_input("Enter the name of the grocery: ")
        if not is_input_string(name):
            continue
        break

    while True: 
        count = get_user_input("Enter the quantity: ")
        if not is_input_positive_digit(count):
            continue
        break

    return name.lower(), int(count)

def add_grocery_item(name, count):
    if name in groceries:
        groceries[name] += count
        return count
    else:
        groceries[name] = count

def substract_grocery_item(name, count):
    if name in groceries:
        if groceries[name] >= count:
            groceries[name] -= count
            if groceries[name] == 0:
                del groceries[name]
        else:
            print("you took too much, you dont have that many")
    else:
        print("this item is not in your fridge. ")

def rename(name):
    if name in groceries:
        response = get_user_input("Enter new name: ")
        new_name = response.title()
        groceries[new_name] = groceries[name]
        del groceries[name]
        print(f"Renamed '{name}' to '{new_name}'")
    else:
        print("You cannot rename some that doesnt exist")



def log_groceries():    
    for name, quantity  in groceries.items():
        print(f"- {name}: {quantity } ks")


def is_input_string(text):
    if text.isalpha():
        return True
    else:
        print("Your log needs to have only letters")
        return False

def is_input_positive_digit(text):
    if text.isdigit() and int(text) > 0:
        return True
    else:
        print("Your log may have only positive number")
        return False
    

main()