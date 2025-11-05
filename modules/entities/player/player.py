from pygame import image, transform
from modules.keybindings import *


class Player:
    def __init__(self, x, y, image_path, width=80, height=80):
        self.x = x
        self.y = y
        self.v = 10
        self.image = image.load(image_path).convert_alpha()
        self.image = transform.scale(self.image, (width, height))
        self.width, self.height = self.image.get_size()

    def handle_movement(self, keydn, screen_width):
        dx = 0
        if keydn[A]:
            dx = -1
        if keydn[D]:
            dx = 1
        self.x += dx * self.v
        self.x = max(0, min(screen_width - self.width, self.x))

    def draw(self, master):
        master.blit(self.image, (self.x, self.y))
