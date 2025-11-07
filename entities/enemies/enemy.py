from modules.entities.entity import Entity
from modules.entities.items.scrap import Scrap
from pygame import Surface

"""enemy.py: A template for creating enemy entities."""

__author__ = "Gustav Vising"

class Enemy(Entity):

    # Variables that will be initialized
    enemy_health = -1
    enemy_spawn_position_x = -1
    enemy_spawn_position_y = -1
    enemy_maximum_allowed_right = -1
    enemy_maximum_allowed_left = -1

    # Constants
    enemy_delay_between_fire = 3  # Seconds between firing projectiles
    enemy_maximum_horizontal_movement = (
        10  # Both left and right from the spawn position
    )
    enemy_y_moving_direction = 1  # The enemy moves downwards

    # Changing variables
    enemy_x_moving_direction = -1

    def __init__(
        self,
        name: str,
        img_path: str,
        width: int,
        height: int,
        x: int,
        y: int,
        health: int,
    ):
        super().__init__(name,img_path,width,height,x,y)

        # Entity class variables
        self.name = name
        self.img_path = img_path
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Enemy class variables
        self.enemy_health = health
        self.enemy_spawn_position_x = x
        self.enemy_spawn_position_y = y

        # Calculate values
        self.enemy_maximum_allowed_right = x + self.enemy_maximum_allowed_right
        self.enemy_maximum_allowed_left = x - self.enemy_maximum_allowed_left

        # Spawn position
        self.set_position(x, y)

    def update(self, screen: Surface):

        # Move
        if self.x <= self.enemy_maximum_allowed_left:
                self.enemy_x_moving_direction = 1
        elif self.x >= self.enemy_maximum_allowed_right:
                self.enemy_x_moving_direction = -1

        self.x += self.enemy_x_moving_direction
        self.y += self.enemy_y_moving_direction

        # Fire projectile here

        # Alive
        if self.enemy_health <= 0:
            
            # Turn the enemy into a scrap
            Scrap("scrape","images/scrap.png",200,200,self.x,self.y)
            
            # Remove the enemy
            Entity.entity_dic.pop(self.name)

