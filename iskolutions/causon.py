from os import system
import random

UNSET_OPTION = -1
EXIT_OPTION = 4

def display_get_choice():
    print("==========Miko Lorenz O. Causon==========")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Password Checker")
    print("4. Exit")
    print("=========================================")
    
    try:
        choice = int(input("Enter your choice: "))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input! Please enter a number.")
        return UNSET_OPTION

def process_choice(choice):
    match choice:
        case 1:
            display_basic_info()
        case 2:
            display_goals()
        case 3:
            # TODO: implement password checker
            pass
        case 4:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")
            pass
        
def display_basic_info():
    system("cls")
    print("Name: Miko Lorenz O. Causon")
    print("Sex: Male")
    print("Birthday: June 9, 2005")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    input("\n Press Enter to Continue...")
    
def display_goals():
    system("cls")
    print("Long-term goals:")
    print("Secure a high paying job.")
    print("Build and grow professional network through LinkedIn and " 
          + "other means.")
    print("Move to a more comfortable house.")
    print("Be financially independent.")
    print("\nShort-term Goals")
    print("Pass INTE 202.")
    print("Save enough money to upgrade laptop.")
    print("Create a project to strengthen portfolio.")

def miko():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)