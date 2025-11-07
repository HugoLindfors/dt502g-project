from entities.enemies.enemy import Enemy

"""enemy.py: A special case of the class enemy"""

__author__ = "Gustav Vising"

class Boss(Enemy):

    def __init__(self):

        name = "Boss"
        img_path = "images/ship.png"
        width = 100
        height = 100
        x = 50
        y = 50
        health = 30

        super().__init__(name,img_path,width,height,x,y, health)
