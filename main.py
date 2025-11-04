import sys
import os

"""
This allows the code to omit the first modules folder from the imports, i.e. import entities instead of import modules.entities.
"""
modules_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "modules"))
sys.path.insert(0, modules_path)

from math import sqrt
import pygame
from pygame import Color, display, event, image, key, transform
from pygame.time import Clock


# STATIC VARIABLES
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
ORANGE = Color(255, 127, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
CYAN = Color(0, 255, 255)
BLUE = Color(0, 0, 255)
MAGENTA = Color(255, 0, 255)
WHITE = Color(255, 255, 255)


pygame.init()

# SCREEN SETUP
info = display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
display.set_caption("DT502G Project - The Game")

# LOAD AND SCALE PLAYER IMAGE
player_image = image.load("images/player.png").convert_alpha()

# RESIZE IMAGE
player_image = transform.scale(player_image, (80, 80))
player_width, player_height = player_image.get_size()


x, y = 200, 200
v = 10

loop_should_break = False
clock = Clock()


while not loop_should_break:

    for evt in event.get():
        if evt.type == pygame.QUIT:
            loop_should_break = True

    display.flip()

    clock.tick(60)

pygame.quit()
