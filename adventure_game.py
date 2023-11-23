from character_module import Character

class Story:

    def __init__(self):
        self.current_location = "Farm"
        self.player = None

    def start_story(self):
        print("Welcome to the story!")
        print("Before u begin your adventure create a new character.")
        self.player = create_character()
        print("Your adventure has started!")

    def get_location(self):
        return self.current_location 
    
    def move(self, new_location):
        print(f"You moved from {self.current_location} to {new_location}.")
        self.current_location = new_location
        self.explore_location()

    def explore_location(self):
        print(f"You are exploring location: {self.current_location}.")

        if self.current_location == "Farm":
            print("On the farm you see a field full of grain and a flock of sheep.")
            print("What are you going to do?")
            print("1. Harvest the grain")
            print("2. Fedd a sheep")
            print("3. Go to the next location")

            choice = input("Enter number of your choice: ")
            self.handle_farm_choice(choice)

    def handle_farm_choice(self, choice):
        if choice == "1":
            print("You harvest the grain! You gain 10 gold.")
            self.player.gain_gold(10)
        elif choice == "2":
            print("You fedd a sheep! You gain 5 gold.")
            self.player.gain_gold(5)
        elif choice == "3":
            self.move("Forest")
        else:
            print("Invalid choice. Try it again.")

def create_character():
        name = input("Enter name of your character: ")

        print("Choose your class: ")
        print("1. Knight")
        print("2. Mage")
        print("3. Ranger")

        class_choice = int(input("Enter the class number: "))

        if class_choice == 1:
            char_class = "Knight"
        elif class_choice == 2:
            char_class = "Mage"
        elif class_choice == 3:
            char_class = "Ranger"
        else:
            char_class = "Uknown"

        return Character(name, char_class, level=1, xp=0, gold=0)

def main():
    game_story = Story()
    game_story.start_story()

    while True:
        print("Current location: " + game_story.get_location())
        print("What do you want to do?")
        print("1. Move to the next location")
        print("2. Show information about character")
        print("3. End game")

        choice = input("Enter number of your choice: ")

        if choice == "1":
            new_location = input("Enter new location: ")
            game_story.move(new_location)
        elif choice == "2":
            game_story.player.display_info()
        elif choice == "3":
            print("Game over. Thank you for playing!")
            return
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()