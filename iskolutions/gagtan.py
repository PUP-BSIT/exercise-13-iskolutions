from os import system
import random

UNSET_OPTION = -1
EXIT_OPTION = 4

def get_choice():
    system("cls")
    print("=============Hanz Matthew A. gagtan =============")
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

def hanz():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = get_choice()
        process_choice(choice)
