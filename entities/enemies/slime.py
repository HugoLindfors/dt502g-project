from entities.enemies.enemy import Enemy

"""slime.py: A special case of the class enemy"""

__author__ = "Gustav Vising"

class Slime(Enemy):

    def __init__(self):

        name = "Slime"
        img_path = "images/slime.png"
        width = 100
        height = 100
        x = 50
        y = 50
        health = 1

        super().__init__(name,img_path,width,height,x,y, health)
