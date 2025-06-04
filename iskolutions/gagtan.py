from os import system
import random

UNSET_OPTION = -1
EXIT_OPTION = 6

def get_choice():
    system("cls")
    print("=============Hanz Matthew A.Gagtan=============")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Advice Generator")
    print("4. Comment from Causon")
    print("5. Comment from Efondo")
    print("6. Exit")
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
            display_causon_comment()
        case 5:
            display_efondo_comment()
        case 6:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")

def display_basic_information():
    system("cls")
    print("Name: Hanz Matthew A.Gagtan")
    print("Gender: Male")
    print("Birthday: February 5, 2005")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    print("Hobbies: Playing guitar, composing songs, and gaming")
    input("\nPress enter to continue...")

def display_goals():
    system("cls")
    print("1. Become a skilled Frontend developer")
    print("2. Travel the world and explore new cultures")
    print("3. Build a successful career in tech and other industries")
    print("4. Support my family and my Community")
    input("\nPress enter to continue...")

def advice_generator():
    system("cls")
    advices = [
        "Keep pushing forward!",
        "Consistency beats motivation.",
        "Rest is productive too.",
        "You are capable of great things.",
        "Start small, but start now.",
        "Don’t compare your Chapter 1 to someone else’s Chapter 10.",
        "Growth happens when you're uncomfortable.",
        "Discipline will take you places motivation can't.",
        "You don’t have to be perfect—just keep showing up."
    ]

    input("Press Enter to get advice...")
    print("\nHanz says:", random.choice(advices))
    input("\nPress Enter to go back...")
    
def display_causon_comment():
    print("Comment from Causon: ")
    print("Don't give up and study even harder! We are always here for you!")
    input("\nPress Enter to Continue...")

def display_efondo_comment():
    print("Comment from Efondo: ")
    print("Don’t stop now, Keep pushing forward and study even harder!")
    input("\nPress Enter to Continue...")

def hanz():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = get_choice()
        process_choice(choice)