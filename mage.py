class Mage(Character):
    def __init__(self, name):
        super().__init__(name, max_health=100, max_mana=50, level=1, xp=0)
        self.spells = ["Fireball", "Ice Shard", "Arcane Missile"]

    def cast_spell(self, spell_index, target):

        pass