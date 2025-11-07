import pygame
from pygame import image, transform
from modules.entities.entity import Entity

player_id = "player"
class Player(Entity):
    def __init__(self, x, y, image_path, width=80, height=80):

        self.v = 10
        super().__init__(player_id,image_path,width,height,x,y)

    def update(self, screen):
        pass

    def handle_movement(self, keys, screen_width):
        width = self.get_rect().width
        x,y = self.get_position()
        dx = 0
        if keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_d]:
            dx = 1
        x += dx * self.v
        self.set_position(max(0, min(screen_width - width, x)),y)

