import pygame
from pygame import image, transform
from modules.entities.entity import Entity
from modules.entities.projectiles.projectile import Laser

player_id = "player"

class Player(Entity):
    def __init__(self, x, y, width=80, height=80, image_path="images/player.png"):
        super().__init__(player_id, image_path, width, height, x, y)
        self.v = 10

    def handle_movement(self, keys, screen_width):
        dx = 0
        if keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_d]:
            dx = 1
        x, y = self.get_position()
        x += dx * self.v
        self.set_position(max(0, min(screen_width - self.get_rect().width, x)), y)

    def fire(self, event):
        x, y = self.get_position()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Center the laser on the player
            laser_x = x + self.get_rect().width // 2 - 5
            laser_y = y - 5
            Laser(x=laser_x, y=laser_y, width=10, height=30, img_path="images/laser.png", direction=1)
