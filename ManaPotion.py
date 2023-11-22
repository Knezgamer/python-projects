from items import Items


class ManaPotion(Items):
    def __init__(self):
        super().__init__("Mana Potion", "Mana Potion restores mana")

    def use(self, Character):
        Character.mana += 15
        if Character.mana > Character.max_mana:
            Character.mana = Character.max_mana
        print(f"{self.name} has been used by {Character.name}") 