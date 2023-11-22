class Knight(Character):
    def __init__(self, name):
        super().__init__(name, max_health=130, max_mana=30, level=1, xp=0)
        self.spells = ["Slash", "Shield Bash", "Holy Strike"]

    def use_ability(self, ability_index, target):

        pass