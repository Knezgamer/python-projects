import json

def load_character_information():
    with open("character_information.json", "r") as file:
        return json.load(file)

def choose_race():
    information = load_character_information()
    races = information["races"]

    print("Choose a race:")
    for i, race in enumerate(races, start=1):
        print(f"{i}. {race}")

    while True:
        try:
            choice = in(input("Enter the number of the chosen race: "))
            if i <= choice <= len(races):
                return races[choice - 1]
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")