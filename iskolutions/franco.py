import os
import random

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

def basic_information():
    print("BASIC INFORMATION:")
    print_border()
    print("Name: Fernette Pearl Franco")
    print("Age: 19")
    print("Gender: Female")
    print("Occupation: Student (Aspiring Web Developer)")
    print("Location: Bagumbayan, Taguig City, Philippines")
    print("School: Polytechnic University of the Philippines")
    print("Course: Bachelor of Science in Information Technology")

    print_border()
    return_to_main_menu()

def goals():
    print("GOALS:")
    print_border()
    print("1. To become a great web developer.")
    print("2. To contribute to major projects that will be impactful.")
    print("3. To learn new programming languages and frameworks.")
    print("4. To build a personal portfolio website (on going).")

    print_border()
    return_to_main_menu()

def random_fact():
    facts = [
        "Did you know that turtles can breathe through their butts?",
        "Octopuses have three hearts — and two of them stop when they swim.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than its year!",
        "Sloths can hold their breath longer than dolphins can.",
        "A group of flamingos is called a 'flamboyance'.",
        "Sharks existed before trees. Nature said, 'priorities.'"
    ]

    print("RANDOM FACTS:")
    print_border()
    print("Feeling curious? Let's see how your brain handles weird knowledge!")

    while True:
        user_input = input("Do you want a random fact?"
                            + " (yes/no): ").strip().lower()
        print_border()

        if user_input == 'yes':
            fact = random.choice(facts)
            print(f"Here's a mind-blowing fact:\n {fact}")
            break
        elif user_input == 'no':
            second_input = input("Are you sure? I promise it’s worth it!"
                                    + " (yes/no): ").strip().lower()
            print_border()
            if second_input == 'yes':
                fact = random.choice(facts)
                print(f"Expanding your brain...\n {fact}")
            elif second_input == 'no':
                print("Alright... maybe another time, curious cat.")
            else:
                print("Hmm, I didn't quite catch that."
                        + " Please answer with 'yes' or 'no'.")
            break
        else:
            print("Oops! Please answer clearly with 'yes' or 'no'.")

    print_border()
    return_to_main_menu()

def comment_section(comment_id):
    comments = {
        '5': "COMMENT FROM CAUSON:\nIt is nice to use dictionaries in this way,"
                + " good job!", 
        '6': "COMMENT FROM EFONDO:\n", #TODO(Efondo): Add comment here
        '7': "COMMENT FROM GAGTAN:\n", #TODO(Gagtan): Add comment here
        '8': "COMMENT FROM LOPEZ:\n"   #TODO(Lopez): Add comment here
    }

    print_border()
    title = comments.get(comment_id)
    print(title)
    print_border()
    return_to_main_menu()

def pearl():
    menu_options = {
        "1": basic_information,
        "2": goals,
        "3": random_fact,
        "4": lambda: comment_section('5'),
        "5": lambda: comment_section('6'),
        "6": lambda: comment_section('7'),
        "7": lambda: comment_section('8')
    }

    while True:
        clear_screen()

        print("Hello there, I am Fernette Pearl Franco!")
        print_border()
        print("1. Basic Information")
        print("2. Goals")
        print("3. A Random Fact")
        print("4. Comment from Causon")
        print("5. Comment from Efondo")
        print("6. Comment from Gagtan")
        print("7. Comment from Lopez")
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