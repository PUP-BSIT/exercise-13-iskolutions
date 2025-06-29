from iskolutions import causon, efondo, franco, lopez, gagtan
from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6

def display_get_choice():
    print("============Select an Option============")
    print("1. Miko Lorenz O. Causon")
    print("2. Aaron Kyle D. Efondo")
    print("3. Fernette Pearl M. Franco")
    print("4. Hanz Matthew A. Gagtan")
    print("5. Jakim D. Lopez")
    print("6. Exit")
    print("========================================")
    
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
            causon.miko()
        case 2:
            efondo.kyle()
        case 3:
            franco.pearl()
        case 4:
            gagtan.hanz()
        case 5:
            lopez.jakim()
        case 6:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")

def main():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)

main()