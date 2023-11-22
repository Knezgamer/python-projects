from character import Character

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