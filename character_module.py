class Character:
    MAX_LEVEL = 12

    def __init__(self, name, char_class, level, xp, gold):
        self.name = name
        self.char_class = char_class
        self.set_class_stats()
        self.level = level
        self.xp = xp
        self.xp_required = 100
        self.gold = gold

    def set_class_stats(self):
        if self.char_class == "Knight":
            self.max_health = 150
            self.max_mana = 30
        elif self.char_class == "Mage":
            self.max_health = 100
            self.max_mana = 60
        elif self.char_class == "Ranger":
            self.max_health = 120
            self.max_mana = 45
        else:
            self.max_health = 100
            self.max_mana = 50
            print ("Uknown class {self.char_class}. Default variables will be used.")
        
        self.health = self.max_health
        self.mana = self.max_mana

    def is_alive(self):
        return self.health > 0
    
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_required:
            self.level_up()

    def gain_gold(self, amount):
        self.gold += amount
        print(f"{self.name} has gained {amount} gold!")
    
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
            print(f"{self.name} has reached max level!")

    def set_max_level(self, max_level):
        self.MAX_LEVEL = max_level      

    def display_info(self):
        print(f"Character: {self.name} (Class: {self.char_class}, Level: {self.level})")
        print(f"Health: {self.health}/{self.max_health} | Mana: {self.mana}/{self.max_mana}")
        print(f"XP: {self.xp}/{self.xp_required} | Gold: {self.gold}")
