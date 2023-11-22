class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, max_health=110, max_mana=40, level=1, xp=0)
        self.spells = ["Arrow Shot", "Snare Trap", "Eagle Eye"]

    def use_ability(self, ability_index, target):

        pass