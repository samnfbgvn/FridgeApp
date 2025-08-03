from fridgeprogram import FridgeProgram
from fridge import Fridge


if __name__ == "__main__":
    groceries1 = {
        "Salat": 2,
        "Tomato": 4,
        "Peach": 7
    }
    groceries2 = {
        "Milk": 3,
        "Eggs": 12,
        "Butter": 1
    }


  
    first_fridge = Fridge(groceries1)
    first_program = FridgeProgram(first_fridge)

    second_fridge = Fridge(groceries2)
    second_program = FridgeProgram(second_fridge)


    def get_valid_fridge_choice():
        while True:
            choice = input("Which fridge do you want to open? (1 or 2): ")
            if choice.isdigit() and int(choice) in [1, 2]:
                return int(choice)
            else:
                print("Please type 1 or 2.")           

    choice = get_valid_fridge_choice()

    if choice == "1":
        first_program.run()
    elif choice == "2":    
        second_program.run()
    else:
        print("Invalid choice. Closing program.")