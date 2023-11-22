class NPC:
    def __init__(self, name, items_for_sale, gold_rewards):
        self.name=name
        self.items_for_sale=items_for_sale
        self.gold_rewards=gold_rewards

    def sell_items(self, items, Character):
        if items in self.items_for_sale and Character.gold >= items.price:
            Character.gold -= items.price
            Character.inventory.append(items)
            print(f"{self.name} has bought {items.name} for {items.price} gold!")
        else:
            print(f"{self.name} does not have enough gold to buy {items.name}!")
        pass

    def give_reward(self, Character):
        Character.gain_gold(self.gold_rewards)