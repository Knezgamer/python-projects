from character_module import Character


class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, char_class="Ranger", max_health=120, max_mana=45, level=1, xp=0, gold=15)
        self.spells = ["Arrow Shot", "Snare Trap", "Eagle Eye"]

    def use_ability(self, ability_index, target): 

        pass