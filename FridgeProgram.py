import requests
import json

from Fridge import Fridge

class FridgeProgram:
    def __init__(self, fridge, filename="groceries_in_fridge.json"):
        self.fridge = fridge
        self.filename = filename
        self.fridge.load_from_json(self.filename)

    def save_changes(self):
        self.fridge.save_to_json(self.filename)

    def get_user_input(self, message):
        response = input(message)
        return response

    def is_input_string(self, text):
        if all(c.isalpha() or c.isspace() for c in text) and text.strip() != "":
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

        return name, int(count)
    

    def run(self):
        answer = self.get_user_input("Do you wanna now what you have in fridge? Yes/No: ")
        if answer.title() == "Yes":
            print("Your storage:\n")
            self.fridge.log_groceries()
            print("\n")
        else:
            print("Alright, closing the fridge")
            return
        
        self.handle_menu()



    def handle_menu(self):
        while True:
            answer = self.get_user_input(
            "Choose an option:\n"
            "1 = Add item\n"
            "2 = Delete item\n"
            "3 = Rename item\n"
            "4 = Show all items\n"
            "5 = Close fridge\n"
            "-> ")
            
            if answer == "1":
                name, count = self.get_name_and_quantity_input()
                self.fridge.add_item(name, count)
                self.save_changes() 
                self.fridge.log_groceries()

            elif answer == "2":
                name, count = self.get_name_and_quantity_input()
                self.fridge.remove_item(name, count)
                self.save_changes() 
                self.fridge.log_groceries()
                
            elif answer == "3":
                old_name = self.get_user_input("Which item do you want to rename? ")
                new_name = self.get_user_input("Enter new name: ")
                self.fridge.rename_item(old_name, new_name)
                self.save_changes() 
                self.fridge.log_groceries()

            elif answer == "4":
                print("Your items in fridge: ")
                self.fridge.log_groceries()
            
            elif answer == "5":
                print(" Closing the fridge.")
                return
            
            else:
                print(" Invalid input – please type a number between 1 and 5.")

       

                

