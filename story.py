
from character_module import create_character


class Story:
    def start_game():
        print("Welcome to the Adventure Game!")

        player = create_character()

        print(f"You created a character named {player.name} which class is {player.char_class}. You started adventure")