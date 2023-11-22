from character import Character

class Knight(Character):
    def __init__(self, name):
        super().__init__(name, char_class="Knight", max_health=150, max_mana=30, level=1, xp=0, gold=15)
        self.spells = ["Slash", "Shield Bash", "Holy Strike"]

    def use_ability(self, ability_index, target):

        pass