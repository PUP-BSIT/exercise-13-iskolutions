from os import system

UNSET_OPTION = -1
EXIT_OPTION = 4

def display_get_choice():
    print("=== WELCOME TO JAKIM LOPEZ'S PROFILE ===")
    print("1. Get to know me better")
    print("2. Goals in life")
    print("3. ") # TODO: add feature
    print("4. Exit")

    try:
        choice = int(input("Enter your choice:"))
        return choice
    except ValueError:
        print("Invalid input.")
        return UNSET_OPTION

def jakim():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()