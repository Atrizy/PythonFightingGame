class Computer:
    def __init__(self, current_hp):
        self.current_hp = current_hp

    def attack(self):
        return 3

    def get_attacked(self, dmg):
        self.current_hp -= dmg