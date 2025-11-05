import sys
import os

"""
This allows the code to omit the first modules folder from the imports, i.e. import entities instead of import modules.entities.
"""
modules_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".modules"))
sys.path.insert(0, modules_path)

from math import sqrt
import pygame
from pygame import Color, display, event, image, key, transform
from pygame.time import Clock

from modules.entities.entity import Entity
from modules.colors import *
from modules.gui.menu import Menu

entitity_dictionary = Entity.entity_dic

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

loop_should_break = False
clock = Clock()


menu = Menu(
    screen, SCREEN_WIDTH, SCREEN_HEIGHT, "images/game_logo.png", "images/star.png"
)

menu.draw()


while not loop_should_break:
    for evt in event.get():
        if evt.type == pygame.QUIT:

            loop_should_break = True

    for e in entitity_dictionary:
        e.update()
        e.draw()


    display.flip()

    clock.tick(60)

pygame.quit()
