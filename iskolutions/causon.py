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
            # TODO: display basic info
            pass
        case 2:
            # TODO: display goals
            pass
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

def miko():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)