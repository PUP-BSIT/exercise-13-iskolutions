from os import system
import re

UNSET_OPTION = -1
EXIT_OPTION = 6

def display_get_choice():
    system("cls")
    print("==========Miko Lorenz O. Causon==========")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Password Checker")
    print("4. Comment from Efondo")
    print("5. Comment from Gagtan")
    print("6. Exit")
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
            password_checker()
        case 4:
            display_efondo_comment()
        case 5:
            display_gagtan_comment()
        case 6:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")
        
def display_basic_info():
    system("cls")
    print("Name: Miko Lorenz O. Causon")
    print("Sex: Male")
    print("Birthday: June 9, 2005")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    input("\nPress Enter to Continue...")
    
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
    input("\nPress Enter to Continue...")
    
def password_checker():
    system("cls")
    print("Password Checker by Miko")
    password = input("Type a password to check its strength: ")
    
    # checks if the password for the criteria using regex
    has_upper = bool(re.search("[A-Z]", password))
    has_lower = bool(re.search("[a-z]", password))
    has_digit = bool(re.search("\d", password))
    has_special = bool(re.search("[!@#$%^&*(),.?\":{}|<>]", password))
    
    strength_criteria = {
        "With Uppercase?": has_upper,
        "With Lowercase?": has_lower,
        "With Digits?": has_digit,
        "With Special Characters?": has_special
    }
    criterias_passed = sum(strength_criteria.values())
    length = len(password)
    
    for key, value in strength_criteria.items():
        print(f"{key} {'Yes.' if value else 'No.'}")
    
    if length >= 12 and criterias_passed == 4:
        strength = "High" 
    elif length >= 8 and criterias_passed >= 3:
        strength = "Average"
    else:
        strength = "Low"
    
    print(f"Your password strength is: {strength} "
          + f"(Length: {length} Criteria Passed: {criterias_passed})")
    input("\nPress Enter to Continue...")
    
def display_efondo_comment():
    print("Comment from Efondo: ")
    print("Nice use of regex for password checking!")
    input("\nPress Enter to continue...")

def display_gagtan_comment():
    print("Comment from Gagtan: ")
    print("Great job on the password checker!")
    input("\nPress Enter to continue...")

def miko():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)