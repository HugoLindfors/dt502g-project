from modules.entities.entity import Entity
from modules.entities.items.scrap import Scrap
from modules.entities.projectiles.projectile import Laser   
from pygame import Surface

class Enemy(Entity):
    enemy_y_moving_direction = 1  # Moves downward

    def __init__(self, name, img_path, width, height, x, y, health, fires_projectiles: bool):
        super().__init__(name, img_path, width, height, x, y)
        self.enemy_health = health
        self.enemy_fires_projectiles = fires_projectiles
        self.enemy_max_left = x - 50
        self.enemy_max_right = x + 50
        self.enemy_x_direction = -1

    def update(self, screen: Surface):
        # Horizontal movement
        if self.x <= self.enemy_max_left:
            self.enemy_x_direction = 1
        elif self.x >= self.enemy_max_right:
            self.enemy_x_direction = -1

        self.x += self.enemy_x_direction
        self.y += self.enemy_y_moving_direction

        # Fire projectiles (placeholder)
        if self.enemy_fires_projectiles:
           laser = Laser(x=self.x + self.get_rect().width // 2 - 5, y=self.y + self.get_rect().height,direction=-1)


        # Check if dead
        if self.enemy_health <= 0:
            # Spawn scrap at enemy location
            Scrap(x=self.x, y=self.y)
            Entity.entity_dic.pop(self.name)
