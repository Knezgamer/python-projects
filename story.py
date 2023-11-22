
from character_module import create_character


class Story:

    def __init__(self):
        self.current_location = "start"
        self.player = None

    def start_story(self):
        print("Welcome to the story!")
        print("Before u begin your adventure create a new character.")

        self.player = create_character()

        print("Your adventure has started!")

    def get_location(self):
        return self.current_location 
    
    def move(self, new_location):
        self.current_location = new_location

    def show_character_info(self):
        if self.player:
            self.player.display_info()