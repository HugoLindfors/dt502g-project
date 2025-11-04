from entities import Enemy

"""enemy.py: A special case of the class enemy"""

__author__ = "Gustav Vising"

class Boss(Enemy):

    def __init__(self):

        self.name = "Boss"
        self.img_path = "images/boss.jpg"
        self.width = 100
        self.height = 100
        self.x = 50
        self.y = 50
        self.health = 30

        super().__init__()
