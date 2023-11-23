class Enemy:
    def __init__(self, name, health, attack, gold_rewards):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_rewards = gold_rewards

    def is_alive(self):
        return self.health > 0 
    
    def give_reward(self, Character):
        Character.gain_gold(self.gold_rewards)  