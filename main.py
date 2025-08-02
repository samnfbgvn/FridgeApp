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


    first_program.run()
    second_program.run()