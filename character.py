class Character:
    MAX_LEVEL = 12

    def __init__(self, name, max_health, max_mana, level, xp):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.level = level
        self.xp = xp
        self.xp_required = 150

    def is_alive(self):
        return self.health > 0
    
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_required:
            self.level_up()
    
    def level_up(self):
        if self.level < self.MAX_LEVEL:
            self.level += 1
            self.max_health += 10
            self.max_mana += 5
            self.health = self.max_health
            self.mana = self.max_mana
            self.xp_required = int(self.xp_required * 1.5)
            print(f"{self.name} has leveled up to level {self.level}!")
        else:
            print(f"{self.name} has reached level {self.MAX_LEVEL}!")

    def set_max_level(self, max_level):
        self.MAX_LEVEL = max_level      