from entities import Enemy

class Boss(Enemy):

    health = 30
    start_x = 0
    start_y = 0

    def __init__(self):
        super().__init__()

        self.setHealth(self.health)
        self.setPosition(self.start_x, self.start_y)