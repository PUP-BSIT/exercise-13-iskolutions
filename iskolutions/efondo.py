from os import system
import random

UNSET_OPTION = -1
EXIT_OPTION = 5

def get_choice():
    system("cls")
    print("==========Aaron Kyle D. Efondo==========")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Rock, Paper, Scissors")
    print("4. Comment from Causon")
    print("5. Exit")
    print("========================================")

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
            rock_paper_scissors()
        case 4:
            display_causon_comment()
        case 5:
            system("cls")
        case _:
            print("Invalid choice! Please select a valid option.")
            input("Press Enter to continue...")
            system("cls")

def display_basic_information():
    system("cls")
    print("Name: Aaron Kyle D. Efondo")
    print("Gender: Male")
    print("Birthday: June 7, 2004")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    print("Hobbies: Playing volleyball, coding, & watching movies")
    input("\nPress enter to continue...")

def display_goals():
    system("cls")
    print("1. Master web development and modern frameworks")
    print("2. Live a good and healthy life with my family")
    print("3. Continuously learning both personal and professional life")
    print("4. Achieve financial stability and independence")
    input("\nPress enter to continue...")
    
def rock_paper_scissors():
    print("\nROCK, PAPER, SCISSORS By Kyle")

    winning_combo = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    while True:
        player_move = input("\nSelect(rock, paper, or scissors): ").lower()
        if player_move not in winning_combo:
            print("Invalid move. Please try again")
            continue
    
        opponent_move = random.choice(list(winning_combo.keys()))
        print(f"Kyle chose: {opponent_move}")

        if player_move == opponent_move:
            print("It's a tie")
        elif winning_combo[player_move] == opponent_move:
            print("You win!")
        else:
            print("Kyle wins!")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing")
            break

def display_causon_comment():
    print("Good job on your programming journey in INTE 202!"
          + " Keep it up!")
    input("\nPress Enter to Continue...")

def kyle():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = get_choice()
        process_choice(choice)