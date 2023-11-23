from items import Items


class HealingPotion(Items):
    def __init__(self):
        super().__init__("Healing Potion", "Healing Potion restores health")

    def use(self, Character):
        Character.health += 15
        if Character.health > Character.max_health: 
            Character.health = Character.max_health 
        print(f"{self.name} has been used by {Character.name}")  