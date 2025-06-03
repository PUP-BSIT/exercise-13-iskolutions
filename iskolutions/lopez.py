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
    
def process_choice(choice):
    match choice:
        case 1:
            display_information()
        case 2:
            pass # TODO: replace function call
        case 3:
            pass # TODO: replace function call
        case 4:
            pass # TODO: replace function call
        case _:
            pass # TODO: replace function call

def display_information():
    print("Name: Jakim D. Lopez")
    print("Age: 20")
    print("Gender: Male")
    print("Pronouns: He/Him")
    print("Location: Wawa, Taguig City")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    print("\nPress any key to continue...")

def jakim():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)