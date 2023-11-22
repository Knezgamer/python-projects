from story import Story

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
            game_story.show_character_info()
        elif choice == "3":
            print("Game over. Thank you for playing!")
            break
        else:
            print("Invalid choice. Try it again.")

if __name__ == "__main__":
    main()