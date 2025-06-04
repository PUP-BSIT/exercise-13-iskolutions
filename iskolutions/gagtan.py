from os import system
import random

UNSET_OPTION = -1
EXIT_OPTION = 4

def get_choice():
    system("cls")
    print("=============Hanz Matthew A.Gagtan=============")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Advice Generator")
    print("4. Exit")
    print("===============================================")

    try:
        choice = int(input("Enter your choice: "))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input! Please enter a number")
        return UNSET_OPTION

def process_choice(choice):
    match choice:
        case 1:
            display_basic_information()
        case 2: 
            display_goals()
        case 3:
            advice_generator()
        case 4:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")
            
def hanz():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = get_choice()
        process_choice(choice)
