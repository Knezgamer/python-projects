from HealthPotion import HealingPotion
from ManaPotion import ManaPotion
from NPC import NPC
from character import Character


class Story:
    def __init__(self):
        self.current_location = "start"

    def get_location(self):
        return self.current_location
    
    def move(self, new_location):
        self.current_location = new_location