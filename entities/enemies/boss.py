from entities import Enemy

"""enemy.py: A special case of the class enemy"""

__author__ = "Gustav Vising"

class Boss(Enemy):

    def __init__(self):
        super().__init__()

        name = "Boss"
        img_path = "images/boss.jpg"
        width = 100
        height = 100
        x = 50
        y = 50
        health = 30
