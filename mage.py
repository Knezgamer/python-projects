from character import Character


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, char_class="Mage", max_health=100, max_mana=60, level=1, xp=0, gold=15)
        self.spells = ["Fireball", "Ice Shard", "Arcane Missile"]

    def cast_spell(self, spell_index, target):

        pass