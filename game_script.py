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
            choice = int(input("Enter the number of the chosen race: "))
            if i <= choice <= len(races):
                return races[choice - 1]
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def choose_gender():
    information = load_character_information()
    genders = information["genders"]

    print ("Choose your gender:")
    for i, gender in enumerate(genders, start=1):
        print(f"{i}. {gender}")

        while True:
            try:
                choice = int(input("Enter the number of the chosen gender: "))
                if i <= choice <= len(genders):
                    return genders[choice - 1]
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a number.")

def choose_class():
    information = load_character_information()
    classes = information["classes"]

    print ("Choose your class:")
    for i, class_name in enumerate(classes, start=1):
        print(f"{i}. {class_name}")

    while True:
        try:
            choice = int(input("Enter the number of the chosen class: "))
            if i <= choice <= len(classes):
                return classes[choice - 1]
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def choose_spell(character_class):
    information = load_character_information()
    class_spells = information ["class_spells"].get(character_class, [])

    if not class_spells:
        print(f"No spells available for {character_class}.")
        return None
    
    print ("Choose a spell:")
    for i, spell in enumerate(class_spells, start=1):
        print(f"{i}. {spell}")

    while True:
        try:
            choice = int(input("Enter the number of the chosen spell (0 for no spell): "))
            if 0 <= choice <= len(class_spells):
                return class_spells[choice - 1] if choice != 0 else None
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def create_character():
    name = input("Enter the character's name: ")
    race = choose_race()
    gender = choose_gender()
    character_class = choose_class()
    spell = choose_spell(character_class)

    character = {
        "name": name,
        "race": race,
        "gender": gender,
        "level": 1,
        "class": character_class,
        "spell": spell,
        "mana": 100,
        "health": 100,
    }

    return character

def save_game_progress(character):
    with open("character_information.json", "r") as file:
        game_progress = json.load(file)

    game_progress.append(character)

    with open("character_information.json", "w") as file:
        json.dump(game_progress, file, indent=2)

if __name__ == "__main__":
    new_character = create_character()
    save_game_progress(new_character)

    print("The character has been created and game progress has been saved.")