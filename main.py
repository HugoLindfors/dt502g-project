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
from modules.keybindings import *
from pygame import KEYDOWN as KEYDN, QUIT
from modules.entities.player.player import Player


def main():
    entitity_dictionary = Entity.entity_dic

    pygame.init()

    # SCREEN SETUP
    info = display.Info()
    SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    display.set_caption("DT502G Project - The Game")

    loop_should_break = False
    game_started = False
    clock = Clock()

    menu = Menu(
        screen, SCREEN_WIDTH, SCREEN_HEIGHT, "images/game_logo.png", "images/star.png"
    )

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, "images/player.png")

    while not loop_should_break:
        for evt in event.get():
            if evt.type == QUIT:
                loop_should_break = True
            elif evt.type == KEYDN:
                if not game_started:
                    if evt.key == ENTER:
                        game_started = True
                    elif evt.key == ESC:
                        loop_should_break = True
                else:
                    if evt.key == ESC:
                        loop_should_break = True

        if not game_started:
            menu.draw()
            clock.tick(60)
            continue

        keys_pressed = key.get_pressed()
        player.handle_movement(keys_pressed, SCREEN_WIDTH)

        screen.fill(color=BLACK)
        player.draw(master=screen)

        for e in entitity_dictionary:
            e.update()
            e.draw()

        display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
