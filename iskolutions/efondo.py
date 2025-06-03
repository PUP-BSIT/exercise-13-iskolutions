from os import system
import random

def get_choice():
    system("cls")
    print("==========Aaron Kyle D. Efondo==========")
    print("1. Basic Information")
    print("2. Goals")
    print("3. Rock, Paper, Scissors")
    print("4. Exit")
    print("========================================")

def display_basic_information():
    system("cls")
    print("Name: Aaron Kyle D. Efondo")
    print("Gender: Male")
    print("Birthday: June 7, 2004")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    print("Hobbies: Playing volleyball, coding, & watching movies")

def display_goals():
    system("cls")
    print("1. Master web development and modern frameworks")
    print("2. Live a good and healthy life with my family")
    print("3. Continuously learning both personal and professional life")
    print("4. Achieve financial stability and independence")

def rock_paper_scissors():
    print("\nROCK, PAPER, SCISSORS")

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