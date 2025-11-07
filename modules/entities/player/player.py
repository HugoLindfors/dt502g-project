from pygame import image, transform
from pygame.key import ScancodeWrapper
from modules.keybindings import *
from enum import Enum

L, N, R = int(-1), int(0), int(1)


class Player:

    image: Surface
    size: tuple[int, int]
    position: tuple[int, int]
    xpos: int
    ypos: int
    width: int
    height: int

    def __init__(
        self, xpos: int, ypos: int, image_path, image_width=80, image_height=80
    ):
        self.position = self.xpos, self.ypos = xpos, ypos
        self.speed = int(10)
        self.image = image.load(image_path).convert_alpha()
        self.image = transform.scale(self.image, (image_width, image_height))
        self.size = self.width, self.height = self.image.get_size()

    def move(self, keydown, screen_width: int):
        direction = N
        if keydown[A] or keydown[LEFT]:
            direction = L
        if keydown[D] or keydown[RIGHT]:
            direction = R
        self.xpos += direction * self.speed
        self.xpos = max(0, min(screen_width - self.width, self.xpos))

    def draw(self, master):
        master.blit(self.image, self.position)
