from os import system
import requests

UNSET_OPTION = -1
EXIT_OPTION = 6
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "aacae991094d7dae63e3a2b8bba7872c"
HTTPS_STATUS_OK = 200

def display_get_choice():
    system("cls")
    print("=== WELCOME TO JAKIM LOPEZ'S PROFILE ===")
    print("1. Get to know me better")
    print("2. Goals in life")
    print("3. Weather Update")
    print("4. Comment from Causon")
    print("5. Comment from Efondo")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice:"))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("\nInvalid choice! Enter a valid option.")
        return UNSET_OPTION
    
def process_choice(choice):
    match choice:
        case 1:
            display_information()
        case 2:
            display_goals()
        case 3:
            get_weather_information()
        case 4:
            display_causon_comment()
        case 5:
            display_efondo_comment()
        case 6:
            system("cls")
        case _:
            print("Press Enter to continue...")
            input()
            system("cls")

def display_information():
    system("cls")
    print("\nGet to know me better:")
    print("Name: Jakim D. Lopez")
    print("Age: 20")
    print("Gender: Male")
    print("Pronouns: He/Him")
    print("Location: Wawa, Taguig City")
    print("Civil Status: Single")
    print("Nationality: Filipino")
    print("\nPress Enter to continue...")
    input()

def display_goals():
    system("cls")
    print("\nGoals in life:")
    print("-To improve my skills in writing clean, structured, and "
          + " maintainable code")
    print("-To develop real-world systems that support organizations "
          + " and solve practical problems")
    print("-To strengthen my technical foundation for future "
          + " external-facing opportunities")
    print("-To pass INTEG 202 course this 2024-2025 school year")
    print("\nPress Enter to continue...")
    input()

def get_weather_information():
    system("cls")
    print("=== WEATHER UPDATE ===")
    input_city = input("Enter any city around the world that "
                       + "you want to check the weather "
                       + "for (e.g. Taguig): ").strip()

    if not input_city:
        print("\nInvalid input! Enter a valid city name.")
        return None

    weather_data = {}

    # API key from OpenWeatherMap (rate-limited upto 60 calls/minute)
    response = requests.get(f"{WEATHER_BASE_URL}?q={input_city} "
                            + f"&appid={API_KEY}&units=metric")

    if response.status_code == HTTPS_STATUS_OK:
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        weather_data[input_city] = {'temperature': temperature, 
                              'weather': weather}
        print(f"\n{input_city}: {temperature}°C, {weather}")
    else:
        print(f"\nError retrieving weather data for {input_city}. "
              + "Either it is an (1) invalid city or (2) check your "
              + "internet connection and try again.")
        
    print("\nPress Enter to continue...")
    input()
    return weather_data

def display_causon_comment():
    print("Comment from Causon: ")
    print("You really did a good job at studying programming!" 
          + "You even used APIs, keep up the good work!")
    input("\nPress Enter to continue...")

def display_efondo_comment():
    print("Comment from Efondo: ")
    print("You’ve done an amazing job learning programming")
    input("\nPress Enter to continue...")

def jakim():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)