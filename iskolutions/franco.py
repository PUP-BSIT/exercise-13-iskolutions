import os

BORDER = "=" * 47

def clear_screen():
    os.system("cls")

def print_border():
    print(BORDER)

def return_to_main_menu():
    print("Press Enter to return to the main menu...")
    input()

def display_section(func):
    clear_screen()
    func()

def pearl():
    menu_options = {}

    while True:
        clear_screen()
        print("Hello there, I am Fernette Pearl Franco!")
        print_border()
        print("8. Exit")
        print_border()

        choice = input("Please select an option (1-8): ")

        if choice == '8':
            print("Thank you for visiting! Goodbye!")
            break
        elif choice in menu_options:
            display_section(menu_options[choice])
        else:
            print("Invalid choice. Please select a number between 1 and 8.")
            return_to_main_menu()

pearl()
